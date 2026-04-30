import os
import requests
import json
import sys
from pathlib import Path
from datetime import datetime

# Lägg till Shared-mappen i sys.path för att kunna importera PDFGenerator
shared_path = Path(__file__).parent.parent / "Shared"
sys.path.append(str(shared_path))
from pdf_generator import PDFGenerator

# Configuration
BASE_URL = "https://jobsearch.api.jobtechdev.se"
API_KEY = os.getenv("JOBTECH_API_KEY", "") 

class JobHunter:
    def __init__(self, profiles_dir, master_cv_path, master_pb_path):
        self.profiles_dir = Path(profiles_dir)
        self.master_cv_path = Path(master_cv_path)
        self.master_pb_path = Path(master_pb_path)
        self.pdf_gen = PDFGenerator()
        self.profiles = []
        self._load_profiles()

    def _load_profiles(self):
        """Loads all competence profiles from markdown files."""
        for file in self.profiles_dir.glob("*.md"):
            if "Mall" in file.name or file.name.startswith("_"):
                continue
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    title = ""
                    for line in content.split('\n'):
                        if line.startswith("# **Kompetensprofil:"):
                            title = line.replace("# **Kompetensprofil:", "").replace("**", "").strip()
                            break
                    if title:
                        self.profiles.append({
                            "file": file.name,
                            "title": title,
                            "path": str(file),
                            "content": content
                        })
            except Exception as e:
                print(f"Kunde inte ladda {file.name}: {e}")

    def search_jobs(self, query, limit=10):
        """Searches for jobs in Lund (municipality 1281)."""
        endpoint = f"{BASE_URL}/search"
        params = {
            'q': query,
            'limit': limit,
            'municipality': '1281' # 1281 is Lund
        }
        headers = {'accept': 'application/json'}
        if API_KEY: headers['api-key'] = API_KEY
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()
            return response.json().get('hits', [])
        except Exception as e:
            print(f"Fel vid sökning efter '{query}': {e}")
            return []

    def get_ad_details(self, ad_id):
        endpoint = f"{BASE_URL}/ad/{ad_id}"
        headers = {'accept': 'application/json'}
        if API_KEY: headers['api-key'] = API_KEY
        try:
            response = requests.get(endpoint, headers=headers)
            return response.json()
        except: return None

    def export_to_pdf(self, folder_path):
        """Converts any markdown files in the folder to PDF."""
        folder = Path(folder_path)
        md_files = list(folder.glob("*.md"))
        
        if not md_files:
            print("Inga Markdown-filer hittades att konvertera.")
            return

        print("\nKonverterar till PDF...")
        for md_file in md_files:
            pdf_path = md_file.with_suffix(".pdf")
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                success = self.pdf_gen.generate(content, pdf_path, title=md_file.stem)
                if success:
                    print(f"✅ Skapade: {pdf_path.name}")
                else:
                    print(f"❌ Misslyckades med: {md_file.name}")
            except Exception as e:
                print(f"Fel vid konvertering av {md_file.name}: {e}")

    def generate_application(self, ad_id, profile_name):
        ad = self.get_ad_details(ad_id)
        if not ad:
            print("Kunde inte hämta annonsdetaljer.")
            return None

        ad_text = ad.get('description', {}).get('text', '')
        headline = ad.get('headline', 'Jobb')
        employer = ad.get('employer', {}).get('name', 'Arbetsgivare')
        webpage_url = ad.get('webpage_url', 'Länk saknas')
        
        # Load profile and masters
        profile = next((p for p in self.profiles if p['file'] == profile_name), None)
        with open(self.master_cv_path, 'r', encoding='utf-8') as f:
            cv_master = f.read()
        with open(self.master_pb_path, 'r', encoding='utf-8') as f:
            pb_master = f.read()

        # Create output folder
        date_str = datetime.now().strftime("%Y-%m-%d")
        folder_name = f"{date_str} - {employer}".replace(" ", "_").replace("/", "_")
        output_dir = Path(r"H:\My Drive\Obsidian\02 Areas\Arbetsliv\ansökningar") / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save files for tailoring
        with open(output_dir / "annons.txt", "w", encoding="utf-8") as f:
            f.write(f"# {headline}\n\n**Länk till annons:** {webpage_url}\n\n{ad_text}")
            
        print(f"\nGenererar ansökan för: {headline} hos {employer}...")
        print(f"Underlag sparat i: {output_dir}")
        
        # Save prompt for LLM
        prompt = f"""
        Här är en jobbannons:
        ---
        {ad_text}
        ---
        
        Här är mitt Master CV (för övergripande historik):
        {cv_master}
        
        Här är min DETALJERADE kompetensprofil för detta specifika område (använd dessa exempel för att skriva ansökan):
        ---
        {profile['content'] if profile else 'Ingen specifik profil vald.'}
        ---
        
        UPPGIFT:
        1. Skapa ett skräddarsytt personligt brev. Använd de SPECIFIKA resultaten, systemen och metoderna från min kompetensprofil ovan för att bevisa att jag matchar annonsens krav.
        2. Föreslå en anpassad 'Profil'-text till CV:t som lyfter fram rätt erfarenheter för detta jobb.
        3. Om annonsen nämner specifika tekniker eller metoder (t.ex. Excel, MI, Projektledning), leta efter matchande bevis i min kompetensprofil och lyft fram dem tydligt.
        """
        
        with open(output_dir / "ai_prompt.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        
        return output_dir

def main():
    base_path = Path(r"H:\My Drive\Obsidian\02 Areas\Arbetsliv")
    profiles_path = base_path / "Erfarenhetsbank" / "Kompetensprofiler"
    cv_path = base_path / "Master CV.md"
    pb_path = base_path / "Master Personligt brev.md"
    
    hunter = JobHunter(profiles_path, cv_path, pb_path)
    
    # Define focus search terms for Lund (Public & Private)
    focus_terms = [
        "Verksamhetsutvecklare", 
        "Business Analyst", 
        "Change Manager", 
        "Projektledare", 
        "Affärsutvecklare",
        "Implementation Specialist",
        "Socionom", 
        "Samordnare"
    ]
    
    print(f"--- Job Hunter CLI (Fokus: Lund) ---")
    results = []
    
    for term in focus_terms:
        # Find matching profile if it exists, otherwise just use the term
        profile = next((p for p in hunter.profiles if term.lower() in p['title'].lower()), None)
        prof_title = profile['title'] if profile else term
        prof_file = profile['file'] if profile else None
        
        print(f"\nSöker: {prof_title} i Lund...")
        jobs = hunter.search_jobs(term)
        
        if not jobs:
            print("  Inga träffar i Lund just nu.")
            continue
            
        for job in jobs:
            print(f"  [{len(results)}] {job.get('headline')} - {job.get('employer', {}).get('name')}")
            results.append((job.get('id'), prof_file))

    choice = input("\nVälj ett nummer för att generera ansökan (eller 'q' för att avsluta): ")
    if choice.isdigit() and int(choice) < len(results):
        ad_id, prof_file = results[int(choice)]
        output_dir = hunter.generate_application(ad_id, prof_file)
        
        if output_dir:
            print(f"\nAnsökan förberedd i {output_dir}")
            print("OBS: Redigera dina .md-filer (CV/PB) innan du konverterar till PDF.")
            make_pdf = input("Vill du konvertera befintliga .md-filer till PDF nu? (y/n): ")
            if make_pdf.lower() == 'y':
                hunter.export_to_pdf(output_dir)
    else:
        print("Avslutar.")

if __name__ == "__main__":
    main()

import requests
import json
import os
import sys
import argparse
from config import BRICKSET_API_KEY, BRICKSET_USERNAME, BRICKSET_PASSWORD, BRICKSET_USER_HASH

# API Endpoints
BASE_URL = "https://brickset.com/api/v3.asmx"

# --- NYA SÖKVÄGAR FÖR OBSIDIAN ---
# Vi utgår från att skriptet körs från sin egen mapp
# Vi sparar data i 02 Areas relativt till projektets struktur
# Sökväg: H:\My Drive\Obsidian\02 Areas\Lego_Collector
BASE_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../02 Areas/Lego_Collector"))
SETS_DIR = BASE_DATA_DIR
IMG_DIR = os.path.join(BASE_DATA_DIR, "attachments")
# ---------------------------------

def get_user_hash():
    """Loggar in och hämtar en userHash om den inte finns i config."""
    if BRICKSET_USER_HASH:
        return BRICKSET_USER_HASH
    
    url = f"{BASE_URL}/login"
    payload = {
        "apiKey": BRICKSET_API_KEY,
        "username": BRICKSET_USERNAME,
        "password": BRICKSET_PASSWORD
    }
    
    try:
        response = requests.post(url, data=payload)
        data = response.json()
        if data.get("status") == "success":
            return data.get("hash")
        else:
            print(f"Inloggning misslyckades: {data.get('message')}")
            return ""
    except Exception as e:
        print(f"Fel vid inloggning: {e}")
        return ""

def fetch_set_data(set_number, user_hash=""):
    """Hämtar data för ett legoset från Brickset."""
    original_number = set_number
    if "-" not in set_number:
        set_number = f"{set_number}-1"
        
    url = f"{BASE_URL}/getSets"
    params = {
        "setNumber": set_number,
        "extendedData": 1
    }
    
    payload = {
        "apiKey": BRICKSET_API_KEY,
        "userHash": user_hash,
        "params": json.dumps(params)
    }
    
    try:
        response = requests.post(url, data=payload)
        data = response.json()
        
        if data.get("status") == "success" and data.get("matches", 0) > 0:
            return data.get("sets")[0]
        
        print(f"Ingen direktträff på {set_number}, försöker med bredare sökning...")
        params = {"query": original_number, "extendedData": 1}
        payload["params"] = json.dumps(params)
        response = requests.post(url, data=payload)
        data = response.json()
        
        if data.get("status") == "success" and data.get("matches", 0) > 0:
            return data.get("sets")[0]
            
        print(f"Hittade tyvärr inget set med nummer {original_number}.")
        return None
    except Exception as e:
        print(f"Fel vid hämtning av data: {e}")
        return None

def download_image(set_data, set_id):
    """Laddar ner bilden och sparar den lokalt i attachments-mappen."""
    url = set_data.get("image", {}).get("imageURL")
    if not url:
        return ""

    os.makedirs(IMG_DIR, exist_ok=True)
    img_path = os.path.join(IMG_DIR, f"{set_id}.jpg")
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            # Returvärde för Markdown (relativ sökväg för Obsidian)
            return f"./attachments/{set_id}.jpg"
        else:
            return url
    except Exception as e:
        return url

SKICK_OPTIONS = ["New Sealed", "Used", "Used No box", "Lego Moc"]
BYGGAT_OPTIONS = ["William", "filip"]

def fetch_owned_sets(user_hash):
    """Hämtar alla ägda set från 2017 och framåt."""
    url = f"{BASE_URL}/getSets"
    params = {
        "owned": 1,
        "year": "2017,2018,2019,2020,2021,2022,2023,2024,2025,2026",
        "pageSize": 500
    }
    
    payload = {
        "apiKey": BRICKSET_API_KEY,
        "userHash": user_hash,
        "params": json.dumps(params)
    }
    
    try:
        response = requests.post(url, data=payload)
        data = response.json()
        if data.get("status") == "success":
            return data.get("sets", [])
        return []
    except Exception as e:
        return []

def generate_markdown(set_data, local_image_path, skick="", byggat="", force=False):
    """Skapar en Markdown-fil i 02 Areas/Lego_Collector."""
    set_number = f"{set_data['number']}-{set_data['numberVariant']}"
    filename = os.path.join(SETS_DIR, f"{set_data['number']}.md")
    
    if os.path.exists(filename) and not force:
        return
    
    frontmatter = {
        "namn": set_data.get("name", ""),
        "id": set_data.get("number", ""),
        "setID": set_data.get("setID", ""),
        "skick": skick if skick in SKICK_OPTIONS else "",
        "Filer media": local_image_path,
        "Kategori": set_data.get("theme", ""),
        "Tema": set_data.get("subtheme", ""),
        "delar": set_data.get("pieces", 0),
        "Released": set_data.get("year", 0),
        "minifigures": set_data.get("minifigs", 0),
        "byggat": byggat if byggat in BYGGAT_OPTIONS else ""
    }
    
    content = "---\n"
    for key, value in frontmatter.items():
        if isinstance(value, str):
            val_escaped = str(value).replace('"', '\\"')
            content += f'{key}: "{val_escaped}"\n'
        else:
            content += f'{key}: {value}\n'
    content += "---\n\n"
    
    content += f"# {set_data['name']} ({set_number})\n\n"
    content += f"![{set_data['name']}]({local_image_path})\n\n"
    
    if set_data.get("extendedData", {}).get("description"):
        content += f"**Beskrivning:** {set_data['extendedData']['description']}\n\n"
    
    content += f"[Se på Brickset]({set_data.get('bricksetURL', '')})\n"
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Sparade {filename}")

def update_dashboard_data():
    """Genererar en databas-fil för HTML-dashboarden."""
    all_sets = []
    if not os.path.exists(SETS_DIR):
        return
        
    for file in os.listdir(SETS_DIR):
        if file.endswith(".md"):
            try:
                with open(os.path.join(SETS_DIR, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    sections = content.split("---")
                    if len(sections) < 3: continue
                    lines = sections[1].strip().split("\n")
                    set_info = {}
                    for line in lines:
                        if ":" in line:
                            k, v = line.split(":", 1)
                            set_info[k.strip()] = v.strip().strip('"')
                    all_sets.append(set_info)
            except: continue
    
    # Dashboard-datan sparas nu i samma mapp som Markdown-filerna (02 Areas)
    output_path = os.path.join(SETS_DIR, "sets_data.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"const legoData = {json.dumps(all_sets, indent=2)};")

def set_collection_status(user_hash, set_id, own=None, want=None):
    """Uppdaterar status för ett set i användarens samling på Brickset."""
    url = f"{BASE_URL}/setCollection"
    
    params = {}
    if own is not None:
        params["own"] = "1" if own else "0"
    if want is not None:
        params["want"] = "1" if want else "0"
        
    payload = {
        "apiKey": BRICKSET_API_KEY,
        "userHash": user_hash,
        "setID": set_id,
        "params": json.dumps(params)
    }
    
    try:
        response = requests.post(url, data=payload)
        data = response.json()
        if data.get("status") == "success":
            status_text = []
            if own is not None: status_text.append("ägt" if own else "ej ägt")
            if want is not None: status_text.append("önskat" if want else "ej önskat")
            print(f"Uppdaterade Brickset-samling: {', '.join(status_text)}")
            return True
        else:
            print(f"Kunde inte uppdatera samling: {data.get('message')}")
            return False
    except Exception as e:
        print(f"Fel vid uppdatering av samling: {e}")
        return False

def import_from_file(file_path, user_hash, force=False):
    """Läser set-nummer från en fil, synkar nya set och flyttar dem till en 'synkad' sektion."""
    if not os.path.exists(file_path):
        print(f"Hittade inte filen: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_numbers = []
    already_synced = []
    header_comments = []
    is_synced_section = False

    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue
        
        if "--- SYNCED" in clean_line:
            is_synced_section = True
            continue
            
        if clean_line.startswith("#"):
            if not is_synced_section:
                header_comments.append(line)
            continue

        num = clean_line.split("#")[0].strip()
        if num:
            if is_synced_section:
                already_synced.append(num)
            else:
                new_numbers.append(num)

    if not new_numbers:
        print("Inga nya set att synka ovanför markeringslinjen.")
        return

    print(f"Bearbetar {len(new_numbers)} nya set...")
    newly_synced = []
    failed = []

    for num in new_numbers:
        data = fetch_set_data(num, user_hash)
        if data:
            if set_collection_status(user_hash, data['setID'], own=True):
                newly_synced.append(num)
                # Skapa MD om den saknas
                filename = os.path.join(SETS_DIR, f"{num}.md")
                if not os.path.exists(filename) or force:
                    img = download_image(data, data['number'])
                    generate_markdown(data, img, force=force)
            else:
                failed.append(num)
        else:
            failed.append(num)

    # Skriv tillbaka till filen med ny struktur
    with open(file_path, "w", encoding="utf-8") as f:
        for comment in header_comments:
            f.write(comment)
        
        if failed:
            f.write("\n# --- MISSING OR FAILED ---\n")
            for f_num in failed:
                f.write(f"{f_num}\n")
        
        f.write("\n# --- SYNCED TO BRICKSET ---\n")
        # Kombinera de nya lyckade med de gamla
        all_synced = list(dict.fromkeys(newly_synced + already_synced))
        for s_num in all_synced:
            f.write(f"{s_num}\n")

    print(f"Filen {os.path.basename(file_path)} har uppdaterats och sorterats.")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LEGO Collector Tool")
    parser.add_argument("number", nargs="?", help="Set-nummer att hämta")
    parser.add_argument("--skick", choices=SKICK_OPTIONS, help="Skick på setet")
    parser.add_argument("--byggat", choices=BYGGAT_OPTIONS, help="Vem som byggt setet")
    parser.add_argument("--sync", action="store_true", help="Synka alla ägda set från 2017+")
    parser.add_argument("--force", action="store_true", help="Skriv över befintliga filer")
    parser.add_argument("--own", action="store_true", help="Markera som ägt på Brickset")
    parser.add_argument("--want", action="store_true", help="Lägg till i önskelistan på Brickset")
    parser.add_argument("--import_file", help="Importera set från en textfil (t.ex. docs/collection_list.txt)")
    
    args = parser.parse_args()
    
    from config import check_config
    check_config()
    
    h = get_user_hash()
    if not h:
        print("Kunde inte verifiera användare. Avbryter.")
        sys.exit(1)
        
    if args.import_file:
        import_from_file(args.import_file, h, force=args.force)
    elif args.sync:
        owned_sets = fetch_owned_sets(h)
        print(f"Hittade {len(owned_sets)} set. Synkar...")
        for s in owned_sets:
            img = download_image(s, s['number'])
            generate_markdown(s, img, force=args.force)
    elif args.number:
        data = fetch_set_data(args.number, h)
        if data:
            # Uppdatera samling på Brickset om flaggor skickats
            if args.own or args.want:
                set_collection_status(h, data['setID'], own=True if args.own else None, want=True if args.want else None)
            
            img = download_image(data, data['number'])
            generate_markdown(data, img, skick=args.skick, byggat=args.byggat, force=True)
    else:
        parser.print_help()
        
    update_dashboard_data()

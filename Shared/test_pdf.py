import sys
import os
from pathlib import Path

# Lägg till mappen i sys.path för att kunna importera pdf_generator
sys.path.append(str(Path(__file__).parent))

from pdf_generator import PDFGenerator

def test_cv_conversion():
    gen = PDFGenerator()
    cv_path = Path(r"H:\My Drive\Obsidian\02 Areas\Arbetsliv\Master CV.md")
    output_path = Path(r"H:\My Drive\Obsidian\02 Areas\Arbetsliv\Master_CV_TEST.pdf")
    
    if not cv_path.exists():
        print(f"Hittade inte CV: {cv_path}")
        return

    print(f"Läser {cv_path}...")
    with open(cv_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    print(f"Genererar PDF till {output_path}...")
    success = gen.generate(md_content, output_path, title="Filip Rodenstam - CV")
    
    if success:
        print("✅ PDF genererades framgångsrikt!")
    else:
        print("❌ Ett fel uppstod vid PDF-genereringen.")

if __name__ == "__main__":
    test_cv_conversion()

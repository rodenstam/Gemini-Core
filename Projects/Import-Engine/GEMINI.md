---
id: import-engine
version: 4.0
type: project
dependencies:
  - shared: gdrive_helper.py
  - shared: gdrive_import_tool.py
stats:
  success_rate: 0.98
  last_run: 2026-05-01
---
# 📥 Project: Import-Engine (Nexus)

## Context
Detta projekt hanterar logiken för att migrera och synkronisera material från Google Drive till Obsidian-valvet. Det fungerar som systemets "ingestions-motor" och säkerställer att allt källmaterial följer en strikt PARA-struktur med lokala bilagor.

## Agent Mandates
1. **Flat Attachments:** Följ ALLTID den platta modellen för `attachments/`-mappar enligt `IMPORT_STRUCTURE.md`.
2. **WikiLink Priority:** Alla länkar i importerade dokument ska vara på formatet `[[Filnamn]]`. Inga absoluta sökvägar eller externa Drive-länkar i brödtexten.
3. **Digital Twin Logic:** Inkludera alltid en info-box för "Digital Tvilling" med länk till Drive-originalet i dokumentets början om det rör sig om ett arkivprojekt.
4. **Cleanup Protocol:** Efter en lyckad import ska `attachments/Originals/` rensas om inte användaren uttryckligen ber om att behålla dem.

## Technical Specs
- **Markdown Conversion:** Google Docs, .docx och .rtf konverteras via Pandoc.
- **Automated Exports:**
    - GSlides -> PDF
    - GSheets -> XLSX
- **Frontmatter:** Alla importerade filer ska ha YAML-metadata (`type: imported_document`).
- **Safety:** Skript får aldrig radera filer baserat på enbart namn; Folder-ID på Drive är den enda säkra identifieraren.

## Primary Commands
- **Bulk Import:** `python "Engine/Importers/bulk_import.py" <folder_id> "<vault_path>"`
- **Single Import:** `python "Engine/Importers/gdrive_import_tool.py" ...` (Se DECISIONS.md för detaljer)

## 🏗️ Folder Structure (PARA Distinction)
Systemet anpassar import-strukturen beroende på vilken PARA-kategori materialet tillhör:

### 📂 01 Projects: Den Platta Modellen (Strikt)
Här används en central `attachments/`-mapp för att hålla projekt-roten ren.
- **Roten:** Endast `[Nav-dokument].md` och aktiva arbetsnoter.
- **`attachments/Sources/`**: Markdown-konverterade källor.
- **`attachments/PDF/`**: Alla PDF-bilagor.
- **`attachments/Presentations/`, `attachments/Sheets/`, `attachments/Images/`**: Specifika binär-mappar.
- **`attachments/Originals/`**: Temporära original inför rensning.

### 📂 02 Areas: Den Direkta Modellen (Integrerad)
Här integreras materialet direkt i ytans befintliga struktur utan den extra `attachments/`-nivån.
- **Placering:** Filer placeras direkt i den relevanta undermappen (t.ex. `Arbetsliv/Erfarenhetsbank/Formella_handlingar/`).
- **Logik:** Följ ytans befintliga mappnamn och kategorisering. Om en lämplig mapp saknas, skapa en beskrivande mapp (t.ex. `Betyg/` eller `Avtal/`) istället för en generisk `attachments/`-mapp.

## ⚖️ Linking Rules
- **Internal Only:** Inga externa Drive-länkar i brödtext. Använd `[[Filnamn]]`.
- **Cleanup:** Vid "Total Migrering" från `00_INKORG`, rensa bort `original_url` och Digital Tvilling-block när materialet är säkrat i Obsidian.



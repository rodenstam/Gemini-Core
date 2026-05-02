---
version: 4.0
type: project
dependencies:
  - shared: gdrive_helper.py
stats:
  success_rate: 1.0
  last_run: 2026-05-01
---
# 🧩 Project: LEGO Collector

## Context
Detta projekt syftar till att bygga ett verktyg för att hämta Lego-data från Brickset API och organisera det i ett Obsidian-valv för samlingshantering och visualisering. Det stödjer nu fullständig synkning av samlingen till Brickset.com.

## Project Structure
- **Management (Planning):** `Workspace/Projects/Lego-Collector/`
- **Engine (Code):** `Projects/Lego-Collector/engine/`
- **Output (Obsidian):** `H:\My Drive\Obsidian\02 Areas\Lego_Collector\`

## Tech Stack
- **Language:** Python 3.13
- **APIs:** Brickset API v3
- **Frontend:** Vanilla HTML/JS (Dashboard)
- **Storage:** Markdown (.md) + Local Images

## Primary Commands
- **Bulk Import:** `python brickset_tool.py --import_file "../docs/collection_list.txt"`
- **Add Single Set:** `python brickset_tool.py <id> --own`
- **Dashboard:** `start ../../../02\ Areas/Lego_Collector/dashboard.html`

## Guidelines
- **The Core Four:** För detta projekt ska dokumentationen primärt vila på fyra pelare i `docs/`:
    1. `SPECS.md` - Långsiktig strategi och faser.
    2. `TASKS.md` - Operativa uppgifter och backlog för utveckling.
    3. `LOG.md` - Logg över genomförda ändringar, beslut och problemlösning.
    4. `DECISIONS.md` - Tekniska kommandon, mallar och API-referenser.
- **Data vs Dokumentation:** `collection_list.txt` betraktas som en datakälla (inkorg/master-lista) och hanteras av skriptet, inte som statisk dokumentation.
- All planering och dokumentation sker i `Lego-Collector\docs\`.
- Skriptet arkiverar automatiskt synkade set under en markör för att spara API-anrop.


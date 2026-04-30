---
type: documentation
project: obsidian-pipeline
status: active
updated: 2026-04-27
---

# ⚙️ Referens: Import-motor & Styrning (v2.0)

Detta dokument beskriver de tekniska komponenterna som styr hur Gemini Core hanterar material från Google Drive till Obsidian.

## 📄 Kritiska Styrdokument (Regelboken)

| Dokument | Syfte |
| :--- | :--- |
| `GEMINI.md` | **Master Context:** Grundregler för autonomi (YOLO-mode) och proaktiv dokumentation. |
| `Rules/IMPORT_STRUCTURE.md` | **Teknisk Spec:** Definierar mappstruktur i Obsidian, länkregler (WikiLinks) och formatval. |

---

## ⚙️ Core Engine (`Engine/Shared/`)

Dessa skript utgör systemets tekniska hjärta och delas av alla moduler. De är byggda för att vara portabla och robusta.

1.  **`gdrive_helper.py`**
    *   **Roll:** Drive-gränssnitt.
    *   **Funktion:** Autentisering (OAuth), export av GDocs och ID-baserad sökning.
2.  **`gdrive_import_tool.py`**
    *   **Roll:** Konverteringslogik.
    *   **Funktion:** Hanterar Pandoc-anrop, städning av Markdown, skapande av Digitala Tvillingar och säkra filnamn.

---

## 🛠 Import-verktyg (`Engine/Importers/`)

Dessa verktyg används för faktiska import-jobb och batch-processer. De ersätter de tidigare experimentella skripten i den "Tunga Pipelinen".

1.  **`bulk_import.py`**
    *   **Funktion:** Rekursiv bulk-import av hela mappar från Drive till ett specifikt Obsidian-projekt. Sorterar automatiskt källfiler och binärer.
2.  **`find_ids.py`**
    *   **Funktion:** Snabbsökning efter mapp-ID:n på Google Drive baserat på namn.
3.  **`list_folder.py`**
    *   **Funktion:** Rekursiv listning av innehåll i en Drive-mapp för att validera struktur innan import.
4.  **`cleanup_imported_links.py`**
    *   **Funktion:** Rensar bort temporära Drive-länkar och Digital Tvilling-metadata från Markdown-filer inför "Total Migrering".

---
*Detta dokument är en del av Gemini Core-arkitekturen och säkerställer ett portabelt och renodlat system.*

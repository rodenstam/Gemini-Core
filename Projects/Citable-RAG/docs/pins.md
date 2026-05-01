# 📌 Pins: Citable-RAG

## Bibliotek
- **PyMuPDF (fitz):** Valts för sin snabbhet och förmåga att läsa annoteringar (highlights).
- **Google Drive API:** Används via `Engine/Shared/gdrive_helper.py`.

## Länksyntax (Obsidian)
- Standard PDF-länk: `[[dokument.pdf#page=5]]`
- Block-referens (teoretisk): `[[dokument.pdf#^blockid]]` (Kräver mer research för binära filer).

## Filstruktur (Planerad)
- `Engine/Citable_RAG/ingestor.py` - Läser in data.
- `Engine/Citable_RAG/brain.py` - RAG-logik och Gemini-koppling.
- `Data/Citable_RAG_Index/` - Lokalt index.

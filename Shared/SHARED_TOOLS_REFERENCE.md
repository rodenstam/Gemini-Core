# 🛠️ Shared Tools: Teknisk Referens

Denna mapp innehåller globala verktyg och motorer som används av flera projekt och agenter inom Gemini-Core. Dessa verktyg är designade för att vara modulära och återanvändbara.

---

## 📄 Centrala Verktyg


### 2. 📑 PDF Generator (`pdf_generator.py`)
En motor för att förvandla Markdown-filer till professionella PDF-dokument med snygg styling.
- **Teknik**: Använder `markdown` och `xhtml2pdf`.
- **Användning**:
  ```python
  from Shared.pdf_generator import PDFGenerator
  gen = PDFGenerator()
  gen.generate(markdown_text, "output.pdf", title="Mitt Dokument")
  ```
- **Styling**: Innehåller inbyggd CSS för att skapa dokument som ser bra ut i Obsidian-miljö.

### 3. 📂 GDrive Helper (`gdrive_helper.py`)
Lågnivå-integration med Google Drive API. Hanterar autentisering och grundläggande filoperationer.
- **Funktioner**:
  - `get_drive_service()`: Hanterar OAuth2-token och returnerar en API-tjänst.
  - `find_file_id_in_robot_folder()`: Söker filer på Drive baserat på namn.
  - `export_gdoc_to_docx()`: Konverterar Google Docs till lokala Word-filer.

### 4. 🚀 GDrive Import Tool (`gdrive_import_tool.py`)
Det primära verktyget för att dra in dokument från Drive till det lokala systemet.
- **Process**:
  1. Laddar ner filen från Drive.
  2. Använder `Pandoc` för att konvertera till Markdown (om det är ett dokument).
  3. Städar upp outputen och lägger till YAML-metadata (Digital Tvilling-länkar).
- **Viktig logik**: `clean_markdown()` tar bort Table of Contents och städar upp formatering för att passa Obsidian.

---

## 🧪 Tester & Verifiering

- **`test_pdf.py`**: Ett enkelt testscript för att verifiera att PDF-genereringen fungerar korrekt med din lokala miljö och typsnitt.

---

## 🧪 Experimental (Under utveckling)

### 1. 🛡️ Core Auditor (`core_auditor.py`)
Systemets "arkitekturväktare". Denna är under aktiv utveckling och bor för tillfället i `Experimental/`.
- **Huvudfunktion**: Validering av mappstrukturer och dokument-integritet.
- **Dokumentation**: Se [CORE_AUDITOR_REFERENCE.md](file:///c:/Gemini-Core/Experimental/CORE_AUDITOR_REFERENCE.md).

---
*Senast uppdaterad: 2026-05-01*

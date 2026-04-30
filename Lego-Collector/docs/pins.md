# 📌 Pins: LEGO Collector

Denna fil innehåller viktiga länkar, koder och mallar för projektet.

---

## 🔗 Dokumentation & API
- **Brickset API v3:** [Documentation](https://brickset.com/article/52664/api-version-3-documentation/)
- **API Endpoint:** `https://brickset.com/api/v3.asmx`

---

## 🏗️ Markdown Mall (YAML Frontmatter)
```yaml
---
namn: "{name}"
id: "{number}"
setID: "{setID}"
skick: ""
"Filer media": "./attachments/{id}.jpg"
Kategori: "{theme}"
Tema: "{subtheme}"
delar: {pieces}
Released: {year}
minifigures: {minifigures}
byggat: ""
---
```

---

## 🛠️ Kommandon (Körs från Engine\Lego_Collector)
- **Visa Dashboard:** `start "H:\My Drive\Obsidian\02 Areas\Lego_Collector\dashboard.html"`
- **Importera från lista:** `python brickset_tool.py --import_file "H:\My Drive\Obsidian\Gemini-Core\Lego-Collector\docs\collection_list.txt"`
- **Hämta & Markera som ägd:** `python brickset_tool.py <id> --own`
- **Hämta & Markera som önskad:** `python brickset_tool.py <id> --want`
- **Synka hela samlingen (2017+):** `python brickset_tool.py --sync`

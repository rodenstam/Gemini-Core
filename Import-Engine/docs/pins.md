# 📌 Pins: Import Engine

## 🔑 Centrala Folder-ID:n (Drive)
- **00_INKORG:** `1jj-X8lKwt-pivh4p8yXAe2MWILeefitl`
- **Arkiv (William):** `1m-W4...` (Exempel)

## 🛠️ Vanliga Kommandon
### Full Bulk Import
Körs från roten av `Gemini-Core`:
```powershell
python "Engine/Importers/bulk_import.py" <folder_id> "H:/My Drive/Obsidian/01 Projects/PROJEKTNAMN"
```

### Städa Länkar
```powershell
python "Engine/Importers/cleanup_imported_links.py" "H:/My Drive/Obsidian/01 Projects/PROJEKTNAMN"
```

### Hitta ID för en mapp
```powershell
python "Engine/Importers/find_ids.py" "Mappnamn"
```

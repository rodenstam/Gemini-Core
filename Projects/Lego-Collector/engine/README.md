# Projekt: LEGO Set Collector

Detta projekt automatiserar hämtningen av LEGO-detaljer från Brickset direkt in i ditt Obsidian-valv.

## Struktur (Ny)
- **Logik (Motorn):** `H:\My Drive\Obsidian\Gemini-Core\Engine\Lego_Collector\`
- **Data (Obsidian):** `H:\My Drive\Obsidian\02 Areas\Lego_Collector\`
- **Bilder:** `H:\My Drive\Obsidian\02 Areas\Lego_Collector\attachments\`

## Kommandon
- **Synka hela din samling:**
  `python "H:\My Drive\Obsidian\Gemini-Core\Engine\Lego_Collector\brickset_tool.py" --sync`

- **Hämta ett specifikt set:**
  `python "H:\My Drive\Obsidian\Gemini-Core\Engine\Lego_Collector\brickset_tool.py" 75192`

- **Hämta med extra info (skick/byggare):**
  `python "H:\My Drive\Obsidian\Gemini-Core\Engine\Lego_Collector\brickset_tool.py" 75192 --skick "New Sealed" --byggat "William"`

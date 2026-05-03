---
id: semantic-search
version: 1.0
type: skill
description: Semantisk sökning och indexering för Gemini-Core.
dependencies:
  - shared: auditor.py
  - data: gemini_keys.env
---
# 🧠 Skill: Semantic Search

Ger systemet ett "fotografiskt minne" genom att förstå innebörden i din kod och dokumentation.

## 🛠️ Hur det fungerar
Systemet använder en tvåstegsprocess för att indexera dina filer:
1.  **Sammanfattning:** `Gemini 3.1 Flash Lite` läser filen och skapar en beskrivning på 2-3 meningar.
2.  **Vektorisering:** Beskrivningen och filnamnet görs om till en matematisk vektor (embedding) via `gemini-embedding-2`.

När du söker jämförs din fråga mot alla sparade vektorer, och de filer som är mest "likt" din fråga visas först.

## 🚀 Kommandon

### Sök i systemet
Använd detta för att hitta kod eller anteckningar baserat på betydelse.
```bash
python Skills/semantic-search/cli.py search "din fråga här"
```

### Indexera filer
Systemet är smart och indexerar bara filer som har ändrats (baserat på MD5-hash).
```bash
python Skills/semantic-search/cli.py index
```
*Tillval:*
- `--root <path>`: Ange en specifik mapp (standard är hela systemet).
- `--silent`: Kör utan terminalutskrift (används för bakgrundsindexering).

## 🛡️ Stabilitet & Automation
- **Lås-mekanism:** En fil `Data/indexer.lock` skapas under indexering för att förhindra krockar mellan bakgrundsprocesser.
- **Auto-indexering:** Gemini-Core kör automatiskt en tyst indexering (`--silent`) vid varje start av `main.py`.

## 🤖 Programmatisk åtkomst (för Agenter)
Agenter kan importera `SearchEngine` direkt för att utföra sökningar utan CLI-overhead:
```python
from Skills.semantic_search.search_engine import SearchEngine
engine = SearchEngine()
results = engine.search("din fråga", top_n=3)
```

## 📂 Tekniska Detaljer
- **Databas:** `Data/semantic_index.db` (SQLite).
- **Credentials:** Kräver `GEMINI_FREE_KEY` i `Data/Credentials/gemini_keys.env`.
- **Modeller:** `gemini-3.1-flash-lite-preview` & `gemini-embedding-2`.

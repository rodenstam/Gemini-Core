# Projekt: LEGO Collector

Detta projekt automatiserar hämtningen av LEGO-detaljer från Brickset API för lokal lagring i Obsidian och fullständig tvåvägssynkronisering av samlingen.

## Målsättning
Att skapa ett sömlöst flöde där fysiska Lego-inköp registreras i en enkel lista, synkas mot Brickset.com och automatiskt genererar rika Markdown-anteckningar med bilder och metadata i Obsidian.

## Systemöversikt
- **Inkorg:** `docs/collection_list.txt` (Här skriver du in set-nummer).
- **Motor:** `Engine/Lego_Collector/brickset_tool.py` (Här bor logiken).
- **Resultat:** `02 Areas/Lego_Collector/` (Här landar dina anteckningar).
- **Visualisering:** En HTML-Dashboard i Obsidian-mappen ger en gallerivy över hela samlingen.

## Hur det fungerar (Logik)
1. **Import:** Skriptet läser nya nummer från listan.
2. **Brickset-synk:** Varje nytt set markeras automatiskt som "Owned" på ditt Brickset-konto.
3. **Berikning:** Metadata (delar, år, minifigurer) och högupplösta bilder hämtas.
4. **Arkivering:** Efter lyckad synk flyttas numret i listan till en "Synced"-sektion för att optimera framtida körningar.

## Metadata-mappning
- **Kategori:** Mappas till Brickset `theme`.
- **Tema:** Mappas till Brickset `subtheme`.
- **SetID:** Det interna Brickset-ID:t sparas alltid för framtida API-interaktioner.

---
*Detta projekt är en del av Gemini Core-ekosystemet.*

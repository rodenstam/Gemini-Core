# 📓 Development Log: LEGO Collector

Denna fil dokumenterar projektets utveckling, tekniska beslut och lösta problem över tid.

---

## 2026-04-25: Omstrukturering & Tvåvägssynk

**Sammanfattning:**
Idag flyttades hela projektets planeringsdel från C-disken till en dedikerad "Ledningscentral" i Obsidian-valvet på H-disken. Samtidigt byggdes kraftfull logik in för att synka samlingen *till* Brickset, inte bara från.

**Genomförda ändringar:**
- Skapat ny struktur: `Gemini-Core/Lego-Collector/docs/` för planering och `Gemini-Core/Engine/Lego_Collector/` för kod.
- Skapat `collection_list.txt` som fungerar som en inkorg för nya Lego-set.
- Uppdaterat `brickset_tool.py` med flaggorna `--own` och `--want` för att uppdatera Brickset-status via API:et `setCollection`.
- Implementerat funktionen `--import_file` för att massimportera set från `collection_list.txt`.

**Tekniska Beslut & Logik:**
- **Dubbletthantering i import:** För att spara API-anrop till Brickset modifierades `import_from_file` funktionen. Istället för att kolla alla set varje gång, skriver skriptet nu om `collection_list.txt` efter en lyckad körning. Färdiga set flyttas ner under rubriken `# --- SYNCED TO BRICKSET ---`. Skriptet läser därefter bara set ovanför denna markör.
- **Tvingad Brickset-synk:** Logiken justerades så att skriptet *alltid* anropar Brickset och sätter `own=1` om ett set ligger i inkorgen, oavsett om Markdown-filen redan existerar lokalt.
- **Nytt Metadata-fält:** Lade till `setID` (Bricksets interna ID) i YAML-frontmattern för framtida API-funktionalitet.

**Lösta Problem:**
- Vid flytt av planeringsfiler uppstod ett internt fel ("Cannot read properties of undefined"). Löstes genom att skriva filerna sekventiellt (en i taget) istället för parallellt.
- Ursprungliga import-logiken skippade Brickset-anropet helt om Markdown-filen fanns, vilket ledde till att Brickset inte uppdaterades. Fixat genom att separera Brickset-anropet från filgenereringen.

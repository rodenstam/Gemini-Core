# 🏛️ Arkitekturplan: Gemini-Core Evolution (v3.0)

## 🎯 Vision: "The Professional Setup"
Att transformera Gemini-Core från en molnbaserad skript-samling till en professionell, högpresterande AI-plattform. Vi separerar **exekvering** (lokal kraft) från **presentation** (Obsidian-vyn).

---

## 🏗️ Den Nya Arkitekturen

### 1. Lokala Basen (C:\Gemini-Core)
*   **Syfte:** "Hjärnan & Musklerna". Här bor all kod, konfiguration och operativ planering.
*   **Prestanda:** Körs direkt från SSD för maximal hastighet.
*   **Backup:** Hanteras via **Git/GitHub**. Ingen direkt-synk med Google Drive på kodenivå för att undvika konflikter.
*   **Mappstruktur:**
    *   `Engine/Shared/`: Globala Python-verktyg.
    *   `Projects/`: Varje projekt (Job-Hunter, Lego, etc.) har sin egen mapp med källkod och lokala `docs/`.
    *   `Skills/`: Modulära förmågor (PDF-motor, Web-scrapers).
    *   `Data/Credentials/`: Lokala API-nycklar (ignoreras av Git).

### 2. Resultat-lagret (H:\My Drive\Obsidian)
*   **Syfte:** "Galleriet & Biblioteket". Här landar alla färdiga resultat som AI:n genererar.
*   **Användning:** Din primära vy för att läsa och navigera i Obsidian (Mobil/Dator).
*   **Innehåll:** Endast Markdown-filer, bilder och PDF:er. Ingen kod eller tekniskt brus.

### 3. Bryggan (Management Mirroring)
*   **Logik:** En automatisk synk-rutin speglar operativ dokumentation (`tasks.md`, `roadmap.md`, `devlog.md`) från `C:` till `H:`.
*   **Nytta:** Du kan läsa status och planer i Obsidian på valfri enhet, men redigering sker via CLI:et på `C:`.

---

## 🗺️ Handlingsplan (Operation: Solid Foundation)

### FAS 1: Etablering (Lokalt på C:)
- [x] Skapa mappstruktur på `C:\Gemini-Core`.
- [x] Kopiera källkod och projekt-mappar från `H:` till `C:`.
- [x] Sätta upp Virtuell Miljö (`.venv`) och installera beroenden.
- [x] Verifiera att skripten kan köras lokalt.

### FAS 2: Git-Integration (Säkerhet)
- [x] Initiera Git-repo i `C:\Gemini-Core`.
- [x] Skapa en strikt `.gitignore` (Skydda nycklar!).
- [ ] Skapa privat GitHub-repo och pusha koden.

### FAS 3: Bryggan & CLI-Lansering
- [ ] Implementera `Mirror-Skill` för dokument-spegling till `H:`.
- [ ] Uppdatera alla projekt-sökvägar till att peka på `H:` för output.
- [ ] Starta den nya `main.py` as central operatörs-hubb.

---
*Fastställd: 2026-04-30*
*Status: Under implementering*

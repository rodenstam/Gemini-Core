# 🏛️ Arkitektur: Gemini Core (v2.1)

Detta dokument beskriver den slutgiltiga och implementerade strukturen för Gemini Core, din centrala hubb för AI-automation och projektstyrning.

## Mål
Att tillhandahålla en stabil, portabel och modulär miljö där **Gemini CLI** fungerar som systemoperatör. Systemet separerar logik (kod) från planering (dokumentation) och resultat (Obsidian-valvet).

## Implementerad Struktur
Systemet bor primärt på `H:\My Drive\Obsidian\Gemini-Core\` för maximal portabilitet via Google Drive.

```text
Gemini-Core/
├── GEMINI.md                   <-- Master Context (Globala regler & YOLO-inställningar)
├── Engine/                     <-- "Maskinrummet" (All körbar logik)
│   ├── Shared/                 <-- Globala verktyg (t.ex. gdrive_helper.py)
│   ├── Lego_Collector/         <-- Python-skript för Lego-hantering
│   └── Obsidian-Pipeline/      <-- Motor för dokumentprocessering
├── Data/                       <-- "Systemminnet"
│   └── Credentials/            <-- API-nycklar och OAuth-tokens
├── Rules/                      <-- "Lagböcker" (Standarder för PARA/Kod/Logik)
├── docs/                       <-- "Långtidsminnet" (Arkitektur, Global DevLog, Roadmap)
│
└── [Projekt-mappar]/           <-- "Ledningscentraler" för specifika projekt
    ├── Lego-Collector/         <-- Planering, Core Four docs & Master List
    └── Obsidian-Pipeline/      <-- Specifik styrning för pipeline-projektet
```

## Tekniska Pelare

### 1. Separation of Concerns (SoC)
- **Management:** Sker i projektmapparnas `docs/`-undermappar (t.ex. `Lego-Collector/docs/`).
- **Execution:** All kod bor i `Engine/` och rör aldrig planeringsfilerna.
- **Output:** Resultat landar direkt i PARA-strukturen (t.ex. `02 Areas/Lego_Collector`).

### 2. Proaktiv Dokumentation
Systemet styrs av ett mandat där Gemini automatiskt uppdaterar eller föreslår uppdateringar av "The Core Four" dokumentation efter betydande förändringar:
1. `SPECS.md` (Strategi)
2. `TASKS.md` (Operativt)
3. `LOG.md` (Historik)
4. `DECISIONS.md` (Teknisk referens)

### 3. Arvshierarki (Context Inheritance)
Den globala `GEMINI.md` definierar systemets driftläge (t.ex. YOLO-mode), medan projekt-specifika `GEMINI.md` finjusterar regler för det enskilda projektet.

## Integrationer
- **Google Drive API:** Centralt för filhantering och molnsynk.
- **Brickset API v3:** Fullständig tvåvägssynk för Lego-samling.
- **Gemini API:** Systemets kognitiva motor för analys och automation.

## Status
- [x] Migrering till H-disk slutförd.
- [x] Engine-arkitektur implementerad.
- [x] Tvåvägssynk för LEGO Collector aktiv.
- [x] Proaktiv dokumentationsregel fastställd.

---
*Senast uppdaterad: 2026-04-25 (Version 2.1 - LEGO Sync & Management update)*

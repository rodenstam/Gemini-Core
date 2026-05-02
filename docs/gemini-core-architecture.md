# 🏛️ Arkitektur: Gemini Core (v4.2)

Detta dokument beskriver den aktuella Manifest-Drivna arkitekturen för Gemini Core (Hybrid Core).

## Mål
Att tillhandahålla en stabil, blixtsnabb och autonom miljö där **Gemini CLI** fungerar som systemoperatör. Systemet separerar exekvering (C:) från presentation/läsning (H: - Obsidian).

## Implementerad Struktur (C:\Gemini-Core)
Systemet bor primärt på den lokala hårddisken för att eliminera latens vid filoperationer och API-anrop.

```text
C:\Gemini-Core/
├── GEMINI.md                   <-- Master Context (v4.2 - YOLO & Regler)
├── Agents/                     <-- Agent-bibliotek (Dialectic Forum-deltagare)
├── Projects/                   <-- Aktiva projekt (Varje projekt har egen docs/ & GEMINI.md)
├── Skills/                     <-- Modulära AI-färdigheter (t.ex. mirror, brainstorming)
├── Shared/                     <-- Globala Python-verktyg (auditor.py, pdf_generator.py)
├── Data/                       <-- Systemminne (session_state.json & Credentials)
├── Workspace/                  <-- Ledningscentral (Management, Strategy, Plans)
└── docs/                       <-- Systemdokumentation (Arkitektur, Global LOG, SPECS)
```

## Tekniska Pelare

### 1. Manifest-Driven Development
- Varje projekt och skill styrs av ett manifest (`GEMINI.md` / `SKILL.md`).
- **Auditor**: `Shared/auditor.py` validerar automatiskt systemets hälsa och beroenden.

### 2. Proaktiv Dokumentation (The Engineering Four)
Systemet vilar på fyra standardiserade pelare för varje projekt i dess `docs/`-mapp:
1. `SPECS.md` (Strategi & Vision)
2. `TASKS.md` (Operativ backlog)
3. `LOG.md` (Historik & DevLog)
4. `DECISIONS.md` (Tekniska beslut & Pins)

### 3. Local State Bus
- Systemet använder `Data/session_state.json` för att hålla reda på aktiva uppgifter och temporär status, vilket gör agenten mer effektiv mellan sessioner.

### 4. Auto-Mirroring (C: -> H:)
- All dokumentation och planer speglas automatiskt till Obsidian via `Skills/mirror/mirror.py` för mänsklig granskning.

## Status
- [x] Migration till v4.2 slutförd.
- [x] "Engineering Four" standardiserad över alla projekt.
- [x] Auditor-stöd för Lite-manifest implementerat.
- [x] Auto-mirror mandate aktivt.

---
*Senast uppdaterad: 2026-05-02 (v4.2 Migration Slutförd)*

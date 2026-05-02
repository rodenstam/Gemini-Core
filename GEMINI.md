---
version: 4.1
type: core
dependencies:
  - skill: mirror
  - shared: auditor.py
stats:
  success_rate: 1.0
  last_run: 2026-05-02
---
# 🏛️ Gemini Core: Master Context (v4.1)

Detta är det centrala operativsystemet för AI-automation. Systemet drivs av en **Manifest-Driven arkitektur** (v4.1) med ett utökat **Agent-Modulärt bibliotek** för Dialectic Forums.

## ⚡️ Driftläge: YOLO (Autonomous Mode)
1. **Local Bus Execution**: All kod och logik körs från `C:\Gemini-Core`. Volatil data lagras i `Data/session_state.json`.
2. **Professional Setup**: Separera exekvering (C:) från presentation (H:).
3. **Manifest-First**: Alla projekt och skills styrs av YAML-manifest för automatisk validering.
4. **Agent-Modulär Struktur**: Vi använder ett bibliotek av specialiserade agenter (`Agents/`) som kan kombineras i Dialectic Forums för att lösa komplexa problem.

## 📂 Systemstruktur (C:\Gemini-Core)
- **`Workspace/`**: Övergripande planering och arkitektur (Speglar till `Management/` i Obsidian).
- **`Projects/`**: Aktiva projekt. Varje projekt är "Self-Describing" via sitt manifest.
- **`Skills/`**: Modulära AI-förmågor. (Speglar till `Skills/` i Obsidian).
- **`Shared/`**: Globala Python-verktyg och hjälpare (t.ex. `auditor.py`).
- **`Data/`**: Systemets minne (Credentials & Session State). **Ignoreras av Git.**
- **`docs/`**: Teknisk systemdokumentation. (Speglar till `System/docs/` i Obsidian).

## 🪞 Speglings-mappning (C: -> H:)
Systemet använder `Skills/mirror/mirror.py` för att hålla Obsidian uppdaterat:
- `Workspace/` -> `Management/`
- `Projects/` -> `Projects/`
- `Skills/` -> `Skills/`
- `docs/` -> `System/docs/`
- Root `.md` -> Root

## 📜 Regler & Mandat
- **Manifest-First**: Innan ett projekt påbörjas eller ändras SKALL dess manifest i `GEMINI.md` valideras eller uppdateras.
- **Sanningen på C**: Alla ändringar i dokumentation SKALL ske på `C:\Gemini-Core`.
- **Auto-Mirror**: Efter att ha skapat eller ändrat en Markdown-fil, KÖR `python Skills/mirror/mirror.py`.
- **Git First**: Alla kodändringar ska commitas till det privata GitHub-repot.
- **Local State Bus**: Agenter SKALL använda `Data/session_state.json` för att spåra aktuell fas, uppgift och temporära variabler för att minska beroendet av stora Markdown-filer för kortsiktigt minne.

---
*Senast uppdaterad: 2026-05-01 (v4.0 Migration Phase 1)*

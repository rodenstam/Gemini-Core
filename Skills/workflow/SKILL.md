---
id: workflow
name: workflow
description: Gemini-Core's Manifest-Driven Workflow. Use this at the start of every task to guide Brainstorming, Planning, and Execution phases.
version: 4.2
type: skill
---
# 🔄 Skill: Workflow (v4.2)

Detta är expertinstruktionerna för hur arbete utförs i Gemini-Core. Aktivera denna skill i början av varje ny huvuduppgift eller när du växlar mellan planering och genomförande.

## 1. 🧠 Brainstorming (Exploration)
- Utforska tills målet och teknisk riktning är 100% tydliga.
- **Dialectic Forum**: Vid arkitektoniska val, aktivera agenter (`Agents/`) för en debatt.
- **The Gate**: Fråga alltid användaren: *"Ska vi gå vidare med Gemini-Core Workflow (Adaptive Planning) för denna uppgift?"*

## 2. 🗺️ Planerings-fasen (Adaptive Planning)
- **Manifest-First**: Kontrollera och uppdatera berörda `GEMINI.md` (projekt) eller `SKILL.md` (skills) INNAN exekvering.
- **YOLO Planning**: Skapa `PLAN_*.md` i `Workspace/Strategy/`. Använd status `utkast`.
- **Ingen CLI Plan Mode**: Undvik `enter_plan_mode` om inte systemet tvingar det. Vi planerar i Markdown direkt på `C:`.

## 3. 🛠️ Exekverings-fasen (Autonomous Mode)
- **Status Flytt**: När genomförandet börjar, ändra status till `pågående` och låt bibliotekarien flytta filen till `Workspace/Plans/Pågående/` via `python Skills/librarian/cli.py fix`.
- **Phase-End Protocol**: Vid varje milstolpe:
    1. Kör tester/validering.
    2. Kör `python Shared/auditor.py`.
    3. Gör en Git Commit.
- **Session State**: Spara transient data (fas-namn, räknare) i `Data/session_state.json`.

## 4. 🏁 Avslutning & Arkivering
- **Manifest Update**: Uppdatera `GEMINI.md` (projekt eller root) för att reflektera slutförd implementering, ändrad version eller nya beroenden. Detta är OBLIGATORISKT för att undvika Context Drift.
- **Status Slutförd**: Sätt status till `slutförd` i planen.
- **Librarian Fix**: Kör `python Skills/librarian/cli.py fix` för att flytta planen till `Workspace/Archive/Plans/Slutförda/`.
- **Auto-Mirror**: Kör ALLTID `python Skills/mirror/mirror.py` som sista steg för att synka Obsidian.

---
*Trigger: Aktiveras när en ny uppgift påbörjas eller vid "The Gate".*

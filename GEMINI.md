# 🏛️ Gemini Core: Master Context (v2.0)

Detta är det övergripande operativsystemet för all AI-automation i ditt Obsidian-valv på Google Drive (`H:\My Drive\Obsidian`).

## ⚡️ Driftläge: YOLO (Autonomous Mode)
1. **Headless Execution**: Motorn ska agera autonomt vid batch-processer. Rapportera i efterhand via loggar istället för att be om godkännande.
2. **Beslutsamhet**: Vid osäkerhet kring PARA-sortering, prioritera mappar i '01 Projects' eller '02 Areas'.
3. **Strikt Output**: Vid databearbetning används uteslutande JSON. Inget kallprat eller förklaringar vid klassificering.

## 📂 Systemstruktur
- **`Engine/`**: Maskinrummet. Innehåller all Python-logik.
    - **`Shared/`**: Globala motorer (t.ex. `gdrive_helper.py`, `pdf_generator.py`).
    - **`Importers/`**: Batch-verktyg för dataimport.
    - **`Job_Hunter/`**: Automatisering av platsbanken och ansökningar.
    - **`Lego_Collector/`**: Metadatahantering för samlingen.
- **`Data/`**: Systemets minne (Credentials & Register).
- **`Rules/`**: Globala standarder.
- **`docs/`**: Arkitektur, loggar och roadmap.

## 🔌 Integrationer
- **PDF Engine (Global)**: Möjliggör konvertering av Markdown till professionella PDF-dokument.
    - *Logik*: `Engine/Shared/pdf_generator.py`
- **JobSearch API (Job Hunter)**: Koppling till Platsbanken för jobbevakning och ansökningsstöd.
    - *Logik*: `Engine/Job_Hunter/job_hunter.py`
- **Google Drive API**: Direkt läsning/skrivning på Drive.
- **Google Gemini API**: Systemets hjärna för analys och textskapande.
- **Brickset API**: Metadata för LEGO-samlingen.

## 📊 Systemstatus
För aktuell status, historik och framtidsplaner, se:
- **`docs/DEV_LOG.md`**: Vad som gjorts under sessionerna.
- **`docs/ROADMAP.md`**: Systemets framtidsplaner.
- **`docs/gemini-core-architecture.md`**: Den tekniska ritningen.

## 📜 Regler & Arv
- **Proaktiv Dokumentation**: Efter varje betydande teknisk förändring, strukturell ändring eller löst problem SKA Gemini antingen uppdatera relevant dokumentation i projektets `docs/` automatiskt eller fråga användaren om en uppdatering ska genomföras.
- **Arvshierarki**: Projekt-specifika `GEMINI.md`-filer ärver grundinställningar från denna fil men har företräde vid specifika instruktioner.
- **Portabilitet**: All kod och alla skript SKALL använda relativa sökvägar för att säkerställa 100% funktion oavsett enhetsbokstav på Google Drive.
- **Språk**: Organisation och metadata sker primärt på svenska.

## 🧠 Filosofi
Vi separerar den **Aktiva Verkstaden** (Gemini-Core) från det **Statisk Biblioteket** (PARA 01-04). Allt som rör AI-utveckling och processering sker inuti Gemini-Core för att hålla PARA-strukturen ren och brusfri. Den gamla "tunga" pipelinen är nu arkiverad i PARA-strukturen för att ge plats åt dagens mer flexibla och portabla import-verktyg.

---
*Senast uppdaterad: 2026-04-27 (Clean Slate & Portabilitet slutförd)*

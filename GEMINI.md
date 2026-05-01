# 🏛️ Gemini Core: Master Context (v3.0)

Detta är det övergripande operativsystemet för all AI-automation. Systemet är nu migrerat till en lokal arkitektur på `C:\Gemini-Core` för exekvering, med spegling till Obsidian-valvet på Google Drive (`H:\My Drive\Obsidian`).

## ⚡️ Driftläge: YOLO (Autonomous Mode)
1. **Local Execution**: All kod och logik körs från `C:\Gemini-Core`.
2. **Professional Setup**: Separera exekvering (C:) från presentation (H:).
3. **Beslutsamhet**: Vid osäkerhet kring PARA-sortering, prioritera mappar i '01 Projects' eller '02 Areas'.
4. **Hybrid Output**: Kommunikation riktad till användaren sker primärt i Markdown. Data som processas mellan system eller i bakgrunden använder JSON.
4. **Agentisk Struktur**: Vi använder "Skills" (instruktioner) och "Agents" (personor) för att styrra AI-arbetet, inspirerat av Superpowers-ramverket.

## 📂 Systemstruktur
- **`Engine/`**: Maskinrummet. Innehåller all Python-logik och verktyg.
- **`Skills/`**: AI-instruktioner (SKILL.md) för specifika arbetsflöden (t.ex. planering, kodning).
- **`Agents/`**: Definitioner av AI-personor (t.ex. "Job Hunter", "Architect").
- **`Shared/`**: Globala hjälpare (t.ex. `gdrive_helper.py`).
    - **`Lego_Collector/`**: Metadatahantering för samlingen.
- **`Data/`**: Systemets minne (Credentials & Register).
- **`Rules/`**: Globala standarder.
- **`docs/`**: Arkitektur, loggar och roadmap.
- **`Workspace/`**: Aktivt arbete, implementationer och tillfälliga filer.

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
*Senast uppdaterad: 2026-05-01 (Lokal Arkitektur C: aktiverad)*

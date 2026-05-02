# Tasks: Job Hunter CLI

## ✅ Avklarat (2026-04-28)
- [x] Flyttat projektstyrning från PARA (01 Projects) till Gemini-Core för renare struktur.
- [x] Implementerat `_KOMPETENSPROFILER_HUB.md` som strategisk överblick för alla kompetensprofiler.
- [x] Konsoliderat `FÖRETAGSINFORMATION.md` och `ANSÖKNINGSINSTRUKTIONER.md` till den gemensamma filen `JOBBINFO.md`.
- [x] Research av Arbetsförmedlingens JobSearch API.
- [x] Grundläggande CLI-motor (`job_hunter.py`) med sök- och hämta-funktion.
- [x] Master CV och Master Personligt brev sammanställda och rensade.
- [x] Integration av lokala kompetensprofiler i ansökningslogiken (Deep Tailoring).
- [x] Implementerat filter för Lund (kommunkod 1281).
- [x] Automatisk generering av ansökningsmappar med annons, instruktioner och AI-prompt.
- [x] Projektstruktur och dokumentation (`GEMINI.md`, `SPECS.md`, `DECISIONS.md`) på plats.

## 🚀 Prioriterat (Fas 1: Automation)
- [ ] Integrera Gemini API direkt i `job_hunter.py` för automatisk textgenerering.
- [x] Skapa en funktion för automatisk PDF-export av ansökningshandlingar (via `pdf_generator.py`).
- [ ] Lägg till stöd för att söka i fler städer än bara Lund (via CLI-argument).

## 🧠 Smartare Matchning (Fas 2: Intelligens)
- [ ] Implementera "Keyword Extractor" som analyserar annonsen innan generering.
- [ ] Möjlighet att kombinera data från flera kompetensprofiler (t.ex. Projektledare + Webbdesigner) baserat på Hub-nodens kategorier.
- [ ] Lägg till bevakning: Skriptet körs en gång per dag och tipsar om nya träffar i Obsidian "Inbox".

## 📊 Överblick (Fas 3: CRM)
- [ ] Skapa en "Job Tracker"-vy i Obsidian med Dataview.
- [ ] Spara historik över alla genererade ansökningar i en central logg-fil.

## 🛠️ Tekniskt underhåll
- [ ] Registrera officiell API-nyckel på JobTech för högre hastighet.
- [ ] Snygga till CLI-gränssnittet med `click` eller `inquirer`.

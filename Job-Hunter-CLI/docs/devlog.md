# Devlog: Job Hunter CLI

## 2026-04-28: Strukturell optimering & Hub-arkitektur

### Genomförda aktiviteter
- **Arkitektonisk flytt:** Flyttade projektets styrfiler (planering, tasks, loggar) från `01 Projects` i PARA-strukturen till `Gemini-Core/Job-Hunter-CLI`. Detta följer projektets filosofi om att separera maskinrummet från biblioteket.
- **Implementering av Hub-nod:** Skapat `_KOMPETENSPROFILER_HUB.md` för att ge en strategisk överblick över alla kompetensprofiler. Detta möjliggör snabbare matchning mot jobbannonser genom att agera som en "Map of Content" (MOC).
- **Förenklad mappstruktur:** Konsoliderat `FÖRETAGSINFORMATION.md` och `ANSÖKNINGSINSTRUKTIONER.md` till en enda fil: `JOBBINFO.md`. Detta minskar filbrus i ansökningsmapparna och förbättrar läsbarheten.
- **Instruktionsuppdatering:** Uppdaterat agent-mandat i `GEMINI.md` för att använda Hub-noden som primär ingångspunkt vid generering av ansökningar (Hub-First approach).

### Strategiska beslut
- **Clean Slate PARA:** Beslutade att hålla `01 Projects` helt fri från systemutvecklingsfiler. Allt som rör AI-verktygens inre logik och projektstyrning ska ligga i `Gemini-Core`.
- **JOBBINFO-standard:** Att samla bakgrund och instruktioner i en fil underlättar när man väl sitter i en ansökningsportal och behöver snabb åtkomst till alla fakta.

---

## 2026-04-28 (Tidigare): Projektstart & Grundarkitektur

### Genomförda aktiviteter
- **Master-data rensning:** Sammanställde spridda CV:n och personliga brev till ett centralt "Master CV" och "Master Personligt brev".
- **API-integration:** Implementerade koppling mot Arbetsförmedlingens JobSearch API.
- **CLI Utveckling:** Byggde `job_hunter.py` för sökningar i Lund (kommunkod 1281).
- **Deep Tailoring:** Implementerade logik för att injicera fullständiga kompetensprofiler i AI-prompter.

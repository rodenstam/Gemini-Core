# Job Hunter CLI - Systemdokumentation

## Syfte
Ett automatiserat verktyg för att hitta relevanta jobbannonser via Arbetsförmedlingens JobSearch API och förbereda skräddarsydda ansökningshandlingar baserat på lokala kompetensprofiler.

## Arkitektur & Filer
- **Motor:** `Engine/Job_Hunter/job_hunter.py` (Python 3.13)
- **Data-källor:**
    - `Master CV.md`: Övergripande arbetshistorik.
    - `Master Personligt brev.md`: Grundton och stil.
    - `Erfarenhetsbank/Kompetensprofiler/*.md`: Detaljerad expertis för specifika yrkesroller.
- **Output:** `ansökningar/[Datum] - [Arbetsgivare]/`
    - `annons.txt`: Den aktuella annonsen.
    - `ai_prompt.txt`: En förberedd prompt för LLM-tailoring.
    - `CV_anpassat.md` / `Personligt_brev.md`: Genererade utkast.

## Användning
1. **Sökning:** Kör `python job_hunter.py`. Skriptet söker automatiskt i Lund efter roller som Verksamhetsutvecklare, Business Analyst, Projektledare m.fl.
2. **Val:** Välj ett jobb genom att skriva in dess indexnummer i listan.
3. **Generering:** Skriptet skapar en mapp med allt underlag och en AI-prompt som inkluderar din mest relevanta kompetensprofil.
4. **Tailoring:** Kopiera prompten till Gemini för att få fram de slutgiltiga dokumenten.

## Konfiguration
- **API:** Använder JobTech JobSearch API.
- **Plats:** Hårdkodat till Lund (municipality 1281).
- **Logik:** Matchar automatiskt sökord mot filnamn i `Kompetensprofiler` för att inkludera rätt djupinformation i prompten.

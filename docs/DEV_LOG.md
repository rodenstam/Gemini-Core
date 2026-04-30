# 📜 Global DevLog: Gemini Core

Här loggas alla större arkitektoniska förändringar och sessioner på systemnivå.

## [2026-04-28] - Job Hunter CLI Integration & PDF Engine (v5.0)
**Status:** Slutförd ✅
**Beskrivning:** Fullständig integration av Job Hunter-projektet i Gemini-Core, driftsättning av PDF-motorn och införande av Hub-arkitektur för kompetensprofiler.

### Genomförda åtgärder:
1.  **Arkitektonisk Konsolidering:** Flyttat projektstyrningen för `Job-Hunter-CLI` från PARA (01 Projects) till `Gemini-Core`. Detta stärker separationen mellan "Maskinrum" och "Bibliotek".
2.  **PDF Engine Deployment:** Verifierat och integrerat `Engine/Shared/pdf_generator.py`. Motorn konverterar nu Markdown till professionella PDF-filer lokalt på under en sekund.
3.  **Hub-arkitektur (MOC):** Skapat `_KOMPETENSPROFILER_HUB.md` som en strategisk överblick (Map of Content) för Erfarenhetsbanken. Infört "Hub-First"-mandat för agenten vid generering av ansökningar.
4.  **CLI Uppgradering:** Uppdaterat `job_hunter.py` med stöd för:
    *   Automatisk extraktion av annons-URL till `annons.txt`.
    *   Interaktiv fråga om PDF-export efter generering.
    *   Sökvägshantering för att inkludera Shared-moduler.
5.  **Strukturförbättring:** Konsoliderat ansökningsmappar genom att slå ihop företagsinfo och instruktioner till en sammanhållen `JOBBINFO.md`.

### Resultat:
- Job Hunter är nu ett högautomatiserat verktyg redo för skarp användning.
- Vi har en fungerande och testad metod för att generera snygga PDF-handlingar utan externa beroenden.
- Kompetensprofilerna har blivit lättare att navigera och använda strategiskt.

---

## [2026-04-26-B] - Strategiskift: PARA-differentierad Migrering (v4.0)
... (resten av filen)

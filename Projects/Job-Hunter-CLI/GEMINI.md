# 🏹 Project: Job Hunter CLI

## Context
Detta projekt automatiserar jobbsökarprocessen genom att koppla ihop Platsbankens API med din personliga kompetensbank i Obsidian. 

## Standard Folder Structure
Varje ansökan ska sparas i `02 Areas/Arbetsliv/ansökningar/[Datum] - [Arbetsgivare]/` och innehålla:
1.  **`annons.txt`**: Den fullständiga annonstexten från Platsbanken.
2.  **`JOBBINFO.md`**: En kombination av företagsinformation (verksamhet, värdegrund) och ansökningsinstruktioner (metod, mottagare, sista dag).
4.  **`ai_prompt.txt`**: Den kompletta prompten med master-data och kompetensprofiler.
5.  **`CV_Filip_Rodenstam_[Arbetsgivare].md`**: Det skräddarsydda CV:t.
6.  **`Personligt_brev_[Arbetsgivare].md`**: Det skräddarsydda personliga brevet (om det efterfrågas).

## Agent Mandates
1. **Lund First:** Prioritera alltid sökningar och annonser i Lund (municipality 1281) om inget annat anges.
2. **Deep Tailoring (Hub-First):** Vid generering av ansökningar, använd ALLTID `_KOMPETENSPROFILER_HUB.md` som utgångspunkt för att identifiera de mest relevanta profilerna. Gör därefter en fördjupning i de valda profilerna i `02 Areas/Arbetsliv/Erfarenhetsbank/Kompetensprofiler/` för att extrahera specifika resultat och bevis. Förlita dig aldrig enbart på Master CV.
3. **Private Sector Focus:** Var proaktiv med att identifiera roller i privat sektor (Business Analyst, Change Manager etc.) för att maximera lönepotentialen, men behåll socionom-grunden för trygghet och samhällsnytta.
4. **Clean Workspace:** Håll `ansökningar/`-mappen strukturerad enligt mönstret `[Datum] - [Arbetsgivare]`.
5. **Job Info Proactivity:** När CV och Personligt brev har genererats i en ansökningsmapp, fråga ALLTID användaren om du ska skapa en sammanfattande `JOBBINFO.md` baserat på annonsen.

## Primary Commands
- **Run Hunter:** `python "../../Engine/Job_Hunter/job_hunter.py"`
- **Config:** Inställningar för sökord finns i `main()`-funktionen i `job_hunter.py`.

## Data Hierarchy
1. **Kompetensprofiler:** Primär källa för yrkesspecifik expertis och bevis.
2. **Master CV:** Källa för kronologisk historik och kontaktuppgifter.
3. **Master Personligt brev:** Källa för språklig ton och personlig presentation.

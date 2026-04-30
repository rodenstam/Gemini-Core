# Pins: Job Hunter CLI

## Snabbreferens
- **API Portal:** [jobtechdev.se](https://www.jobtechdev.se/)
- **API Slutpunkt:** `https://jobsearch.api.jobtechdev.se/search`
- **Kommunkod Lund:** `1281`

## Viktiga kommandon
- **Kör sökning:** `python "H:\My Drive\Obsidian\Gemini-Core\Engine\Job_Hunter\job_hunter.py"`

## Underlag
- **Master CV:** `H:\My Drive\Obsidian\02 Areas\Arbetsliv\Master CV.md`
- **Master PB:** `H:\My Drive\Obsidian\02 Areas\Arbetsliv\Master Personligt brev.md`
- **Kompetensprofiler (Hub):** `H:\My Drive\Obsidian\02 Areas\Arbetsliv\Erfarenhetsbank\Kompetensprofiler\_KOMPETENSPROFILER_HUB.md`
- **Kompetensprofiler (Mapp):** `H:\My Drive\Obsidian\02 Areas\Arbetsliv\Erfarenhetsbank\Kompetensprofiler\`

## LLM Prompt Strategi (Hub-First)
1. **Identifiera:** Använd Hub-noden för att välja de 1-2 mest relevanta profilerna.
2. **Extrahera:** Hämta specifika bevis och resultat från respektive profil-fil.
3. **Injisera:** Placera innehållet i `ai_prompt.txt` tillsammans med Master CV för maximal precision.

# Projektplan: Job Hunter CLI

### **1. Projektbeskrivning & Varför**
- **Namn:** Job Hunter CLI
- **Syfte:** Att effektivisera jobbsökandet genom att automatiskt identifiera relevanta annonser på Platsbanken och generera skräddarsydda ansökningshandlingar (CV och personligt brev) baserat på min befintliga master-data.
- **Slutdatum:** 2026-05-30

### **2. Definition av "Klart" (Mål & Scope)**
- **Huvudmål:** Ett fungerande CLI-verktyg som via API hämtar annonser och producerar färdiga utkast på ansökningar.
- **Leverabler:**
    - Python-skript för kommunikation med Arbetsförmedlingens JobSearch API.
    - CLI-gränssnitt för sökning (t.ex. yrke, plats).
    - Mall-system som injicerar data från `Master CV` och `Kompetensprofiler` i AI-prompter.
    - Funktion för att exportera skräddarsydda `.md`-filer för varje sökt jobb.
- **Out-of-scope:** Automatisk inskickning av ansökningar (sker manuellt), grafiskt gränssnitt (GUI).

### **3. Aktivitetsplan & Milstolpar**
- **Milstolpe 1 (Research):** API-nyckel anskaffad och testanrop mot Platsbanken genomförda. [Datum: Snarast]
- **Milstolpe 2 (Engine):** Grundläggande logik för att matcha annonstext mot relevanta kompetensprofiler klar.
- **Milstolpe 3 (Tailoring):** Integration med Gemini API för att skriva det personliga brevet baserat på annonsen.
- **Milstolpe 4 (Validation):** Testkörning på 3 riktiga annonser med godkänt resultat.

### **4. Resurser & Verktyg**
- **Underlag:**
    - `Master CV.md` & `Master Personligt brev.md`
    - `02 Areas/Arbetsliv/Erfarenhetsbank/Kompetensprofiler/*.md`
- **Verktyg:** Python 3.13, Arbetsförmedlingen JobSearch API, Gemini API, Obsidian.

### **5. Riskhantering**
- **Risk:** API-begränsningar eller förändringar i Arbetsförmedlingens tjänst. -> **Åtgärd:** Bygg modulärt så att datakällan kan bytas ut.
- **Risk:** AI:n blir för generisk i sina brev. -> **Åtgärd:** Använd "Few-shot prompting" med dina tidigare bästa brev som exempel.

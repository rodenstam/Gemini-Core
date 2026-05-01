# 🔄 Gemini-Core Workflow (v3.0)

Detta dokument definierar standardprocessen för hur arbete utförs i Gemini-Core för att säkerställa hög kvalitet, autonomi och kontroll.

## 1. 🧠 Brainstorming-fasen (Exploration)
*   **Syfte:** Att utforska lösningar brett innan beslut fattas.
*   **Process:**
    *   Användaren beskriver ett mål eller problem.
    *   AI:n SKALL söka efter lösningar brett (utanför användarens initiala spår).
    *   Dialogen fortsätter tills ett tydligt mål och en teknisk riktning är fastställd.

## 2. 🗺️ Planerings-fasen (Structured Design)
*   **Syfte:** Att bryta ner lösningen i logiska, hanterbara steg.
*   **Process:**
    *   **Plan-as-a-File:** Varje större initiativ SKALL dokumenteras som en ny `.md`-fil i `Workspace/` (t.ex. `PLAN_PROJECT_X.md`).
    *   Skapa en implementeringsplan uppdelad i **Logiska Faser** med checkboxar.
    *   Varje fas ska vara självständig nog för att kunna valideras.
    *   Planen presenteras för användaren för godkännande.

## 3. 🛠️ Exekverings-fasen (Autonomous Implementation)
*   **Syfte:** Effektivt genomförande med minimal friktion.
*   **Process:**
    *   Användaren aktiverar autonomt läge (`gemini -y`).
    *   AI:n genomför en fas i taget.
    *   **Naturliga Stopp:** Efter varje avslutad fas gör AI:n ett uppehåll.
    *   **Session-Persistence:** AI:n ska dokumentera status så att arbetet kan återupptas i en ny session utan förlust av kontext.

## 4. 🏁 Checkpoint & Review (Human-in-the-loop)
*   **Syfte:** Att validera framsteg och justera kursen.
*   **Process:**
    *   Vid fas-slut går användaren igenom resultatet.
    *   Planen för nästa fas granskas och kan justeras vid behov.
    *   Först efter godkännande av nästa steg återgår systemet till exekvering.

## 5. 🧪 Testning & Kvalitetssäkring (Verification)
*   **Syfte:** Att säkerställa att koden fungerar och är välskriven.
*   **Process:**
    *   Testning sker som en integrerad del av varje fas (inte bara i slutet).
    *   Empirisk verifiering: Kör skriptet, kolla loggar, kontrollera output.
    *   **Code Review:** När funktionaliteten är bekräftad görs en extra genomgång av koden för att säkerställa att den följer systemets standarder och är optimerad.

## 🪞 Spegling & Dokumentation (Mirroring)
*   **Syfte:** Att hålla Obsidian-vyn uppdaterad.
*   **Process:**
    *   Efter varje fas (eller vid naturliga pauser) körs `Mirror-Skill`.
    *   `DEV_LOG.md` uppdateras med de senaste framstegen.

---
*Status: Draft - Under utveckling*
*Senast uppdaterad: 2026-05-01*

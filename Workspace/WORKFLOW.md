# 🔄 Gemini-Core Workflow (v3.1)

Detta dokument definierar standardprocessen för hur arbete utförs i Gemini-Core för att säkerställa hög kvalitet, autonomi och kontroll.

## 1. 🧠 Brainstorming-fasen (Exploration)
*   **Syfte:** Att utforska lösningar brett när det behövs.
*   **Process:**
    *   Användaren beskriver ett mål eller problem.
    *   **Contextual Search:** Om målet är vagt SKALL AI:n söka brett. Om målet är tekniskt specifikt är sökningen valfri.
    *   Dialogen fortsätter tills ett tydligt mål och en teknisk riktning är fastställd.

## 2. 🗺️ Planerings-fasen (Adaptive Planning)
*   **Syfte:** Att bryta ner lösningen i logiska, hanterbara steg.
*   **Process:**
    *   **Size-to-Paperwork:**
        *   *Små uppgifter:* Dokumenteras direkt i `tasks.md`.
        *   *Stora initiativ:* SKALL dokumenteras som en ny `PLAN_*.md`-fil i `Workspace/`.
    *   Skapa en implementeringsplan uppdelad i **Logiska Faser** med checkboxar.
    *   Planen presenteras för användaren för godkännande.

## 3. 🛠️ Exekverings-fasen (Autonomous Implementation)
*   **Syfte:** Effektivt genomförande med inbyggda skyddsnät.
*   **Process:**
    *   **Phase-End Commits:** I autonomt läge gör AI:n en git commit efter varje avslutad fas (om tester passerar).
    *   **Flow-State:** AI:n kör tills ett **Milestone** nås eller ett fel uppstår. Mänsklig review efter varje fas är valfritt.
    *   **Session-Persistence:** AI:n dokumenterar status i `tasks.md` eller `PLAN_*.md` vid session-slut.

## 4. 🧪 Verifiering & Kvalitet (Verification Tiers)
*   **Syfte:** Att säkerställa att koden fungerar och är välskriven.
*   **Process:**
    *   **Tier 1 (Core Logic):** Automatiserade tester är OBLIGATORISKA för delad kod (`Shared/`) och kärnlogik.
    *   **Tier 2 (Utility/Docs):** Empirisk verifiering (loggar, output-kontroll) räcker för hjälp-skript och dokumentation.
    *   **Optimization:** Sker som en del av exekveringen, inte som ett separat obligatoriskt steg i efterhand.

## 🪞 Spegling & Dokumentation (Auto-Mirroring)
*   **Syfte:** Att hålla Obsidian-vyn uppdaterad utan manuell friktion.
*   **Process:**
    *   **Auto-Sync:** `Mirror-Skill` körs automatiskt vid sessionens slut eller vid större milstolpar.
    *   `DEV_LOG.md` uppdateras löpande.

---
*Status: Active (Balanced v3.1)*
*Senast uppdaterad: 2026-05-01*

# 🔄 Gemini-Core Workflow (v4.0)

Detta dokument definierar standardprocessen för hur arbete utförs i Gemini-Core för att säkerställa hög kvalitet, autonomi och kontroll genom en **Manifest-Driven approach**.

## 1. 🧠 Brainstorming-fasen (Exploration)
*   **Syfte**: Att utforska lösningar brett när det behövs.
*   **Process**:
    *   Användaren beskriver ett mål eller problem.
    *   **Contextual Search**: Om målet är vagt SKALL AI:n söka brett. Om målet är tekniskt specifikt är sökningen valfri.
    *   **Dialectic Mode**: Vid komplexa beslut eller arkitektoniska vägval SKALL ett **Dialectic Forum** (`Agents/DIALECTIC_PROTOCOL.md`) aktiveras för att belysa lösningen ur flera perspektiv (t.ex. Architect, Pragmatist, Auditor).
    *   Dialogen fortsätter tills ett tydligt mål och en teknisk riktning är fastställd.
    *   **The Gate**: Innan övergång till Planering SKALL AI:n fråga: *"Ska vi gå vidare med Gemini-Core Workflow (Adaptive Planning) för denna uppgift?"*

## 2. 🗺️ Planerings-fasen (Adaptive Planning)
*   **Syfte:** Att bryta ner lösningen i logiska, hanterbara steg och säkra infrastrukturen.
*   **Process:**
    *   **Manifest-First:** Innan exekvering påbörjas SKALL berörda `GEMINI.md` eller `SKILL.md` manifest kontrolleras och uppdateras vid behov (version, beroenden).
    *   **Size-to-Paperwork:**
        *   *Små uppgifter:* Dokumenteras direkt i `TASKS.md` i projektets `docs/`-mapp.
        *   *Stora initiativ (Globalt):* Utvecklas som en ny `PLAN_*.md`-fil i `Workspace/Strategy/`. Vid slutfört initiativ flyttas filen till `Workspace/Archive/Plans/`.
        *   *Stora initiativ (Projekt):* Utvecklas som en ny `PLAN_*.md`-fil i projektets egen `docs/`-mapp. Vid slutfört initiativ flyttas filen till projektets `docs/Archive/`.
    *   Skapa en implementeringsplan uppdelad i **Logiska Faser** med checkboxar.

## 3. 🛠️ Exekverings-fasen (Autonomous Implementation)
*   **Syfte:** Effektivt genomförande med inbyggda skyddsnät.
*   **Process:**
    *   **Phase-End Protocol:** Vid avslutad fas i en plan SKALL AI:n:
        1. Köra relevanta tester.
        2. Köra `python Shared/auditor.py` (valfritt vid små ändringar, rekommenderat vid strukturella).
        3. Göra en Git Commit med tydlig beskrivning.
    *   **Local State Bus:** Använd `Data/session_state.json` för att lagra volatil status mellan sessioner/faser.
    *   **Flow-State:** AI:n kör tills ett **Milestone** nås eller ett fel uppstår.

## 4. 🧪 Verifiering & Kvalitet (The System Guard)
*   **Syfte:** Att säkerställa att koden fungerar och att systemets integritet bibehålls.
*   **Process:**
    *   **Tier 1 (Core Logic):** Automatiserade tester är OBLIGATORISKA för delad kod (`Shared/`).
    *   **Tier 2 (Audit):** Kör `python Shared/auditor.py` för att validera manifest och beroendegraf efter större ändringar.
    *   **Empirisk verifiering:** Loggar och output-kontroll för skript och dokumentation.

## 5. ⚡ Valfrihet & Flow (Optionality Protocol)
*   **Syfte:** Att behålla snabbhet för enkla uppgifter.
*   **Process:**
    *   Det formella arbetsflödet (Planering/Manifest) KAN hoppas över för:
        *   Snabba frågor och informationssökning.
        *   Små ändringar i Markdown (t.ex. fixa stavfel).
        *   Icke-strukturella buggfixar (one-liners).
    *   Vid minsta osäkerhet eller risk för arkitektonisk drift SKALL det formella flödet följas.

## 🪞 Spegling & Dokumentation (Auto-Mirroring)
*   **Syfte:** Att hålla Obsidian-vyn uppdaterad utan manuell friktion.
*   **Process:**
    *   **Auto-Sync:** `Mirror-Skill` körs automatiskt vid sessionens slut eller vid större milstolpas-slut.
    *   `LOG.md` uppdateras löpande i `docs/`.

---
*Status: v4.0 Active (Manifest-Driven)*
*Senast uppdaterad: 2026-05-01*

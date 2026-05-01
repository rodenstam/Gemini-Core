# 📜 PROPOSAL: Global Constitution (Root GEMINI.md)

## 🏛️ Systemets Arkitektur (C:\Gemini-Core)
Detta dokument fungerar som den högsta lagen för Gemini-Core. Alla projekt SKALL följa dessa globala standarder.

### 1. "Shared-First" Principen
*   **Logik-placering**: Om en funktion eller klass används av mer än ett projekt SKALL den flyttas till `Shared/`.
*   **Import-standard**: Alla projekt refererar till `Shared/` via absoluta eller konfigurerbara sökvägar (ej relativa `../..` om möjligt).

### 2. Säkerhet & Data (Data/Credentials)
*   **Centraliserade Nycklar**: Inga API-nycklar eller `.env`-filer får finnas i projektmappar om de kan delas. De bor i `Data/Credentials/`.
*   **Git-Skydd**: Root `.gitignore` täcker hela systemet. Inget i `Data/` får någonsin pushas.

### 3. Speglings-hierarki (C: -> H:)
*   **Standard-mappning**:
    *   `Workspace/` -> `Management/`
    *   `Projects/[Name]/docs/` -> `Projects/[Name]/`
    *   `Skills/` -> `Skills/`
    *   `docs/` -> `System/docs/`
*   **Responsibilitet**: Varje projekt ansvarar för att dess `docs/` är välstrukturerade för Obsidian-läsning.

### 4. Agent-Direktiv
*   Vid start av en session SKALL agenten läsa denna fil för att förstå systemets aktuella tillstånd och gällande lagar.
*   Workflowet i `Workspace/WORKFLOW.md` är obligatoriskt för alla ändringar.

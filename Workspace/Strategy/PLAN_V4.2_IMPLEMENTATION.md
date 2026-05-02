# 🚀 PLAN: Gemini-Core v4.2 Implementation (Frictionless Integrity)

**Status**: 🗓️ Planerad
**Initiativ**: Migration till v4.2 baserat på Dialectic Forum resultat.
**Mål**: Minska friktion vid dokumentation och öka systemisk integritet genom automatisering.

## 📝 Logiska Faser

### Fas 1: Standardisering (Engineering Four)
Syfte: Skapa en enhetlig struktur för alla projekt för att öka sökbarhet.
- [ ] **Inventering**: Identifiera alla projekt som använder "The Core Four" (Roadmap, Devlog, Tasks, Pins).
- [ ] **Refaktorering**:
    - Byt namn på `ROADMAP.md` -> `SPECS.md`
    - Byt namn på `DEV_LOG.md` -> `LOG.md`
    - Byt namn på `PINS.md` (om den finns) -> `DECISIONS.md`
- [ ] **Länkuppdatering**: Uppdatera interna länkar i manifest (`GEMINI.md`) och andra markdown-filer.

### Fas 2: Lite-Manifest & System-stöd
Syfte: Tillåta snabbare utveckling av små verktyg utan att tappa kontrollen.
- [ ] **Template**: Skapa `Shared/templates/lite_GEMINI.md` som kombinerar manifest och logg i en fil.
- [ ] **Auditor Update**: Uppdatera `Shared/auditor.py` för att:
    - Stödja "Lite"-typen i manifestet.
    - Validera att "Engineering Four" följs för standardprojekt.
- [ ] **Mirror Update**: Uppdatera `Skills/mirror/mirror.py` för att hantera den nya strukturen och Lite-filer.

### Fas 3: Automatisering & Workflow
Syfte: Göra systemet "självläkande" och minska risken för Context Drift.
- [ ] **WORKFLOW.md**: Uppdatera instruktionerna för att inkludera `session_state.json` för transient status.
- [ ] **GEMINI.md (Core)**: Uppdatera master-manifestet till v4.2.
- [ ] **Agent Mandates**: Lägg till instruktioner i `GEMINI.md` att alltid köra `mirror.py` vid avslutad uppgift (YOLO-instruktion).

## 🚀 Exekvering (YOLO-instruktion)
Denna plan ska genomföras stegvis. Vid varje fas-slut ska `Shared/auditor.py` köras och en commit göras. Börja med Fas 1.

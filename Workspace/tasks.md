# 📝 Gemini-Core: Operativ Tasklista

Denna lista hanterar de återstående stegen för att göra alla moduler 100% kompatibla med den nya Arkitektur v4.0.

## 🚀 Prioritet: Operativ Stabilitet (v4.0 Ready)
Målet är att alla val i `main.py` ska fungera felfritt i den nya lokala miljön.

- [ ] **Job-Hunter-CLI**
    - [ ] Verifiera import-sökvägar till `Shared/`.
    - [ ] Uppdatera sökvägar till `Data/Credentials/`.
    - [ ] Testa att köra en sökning från huvudmenyn.
- [ ] **Lego-Collector**
    - [ ] Verifiera databasanslutning (om lokal).
    - [ ] Uppdatera bild- och exportmappar till att peka på `C:`.
    - [ ] Testa start via menyn.
- [ ] **Citable-RAG**
    - [ ] Skapa en `main.py` som fungerar som instegspunkt.
    - [ ] Integrera mot den lokala PDF-motorn i `Shared/`.

## 🧠 Strategisk Utveckling
- [x] **Workflow Definition**
    - [x] Designa standard-workflowet för Gemini-Core (Planering -> Exekvering -> Spegling).
- [ ] **Skills & Agents Setup**
    - [ ] Etablera strukturen för hur nya Skills skapas.
    - [ ] Definiera de första Agent-personorna i `Agents/`. (Arkitekten är klar).
- [ ] **Dokumentations-audit**
    - [ ] Gå igenom alla `GEMINI.md`-filer (root och projekt) för att säkerställa att de matchar v4.0.

## ✅ Genomförda Milstolpar (v4.0 Hybrid Core)
- [x] **Manifest-Migrering**: Designat YAML-schema och uppgraderat alla projekt.
- [x] **System Guard (auditor.py)**: Migrerat till `Shared/`, implementerat beroende-check och schemavalidering.
- [x] **Volatile Memory Layer**: Initierat `Data/session_state.json` för agent-status.
- [x] **Atomic Background Mirroring**: Refaktorerat `mirror.py` till Stage-and-Swap och integrerat i Auditor.
- [x] **Central Hub Upgrade**: Uppdaterat `main.py` till v4.0 med Auditor-integration.
- [x] Migrering till `C:\Gemini-Core`.
- [x] Etablering av privat GitHub-repo.
- [x] Implementering av `Mirror-Skill` (C: -> H:).

---
*Senast uppdaterad: 2026-05-01*

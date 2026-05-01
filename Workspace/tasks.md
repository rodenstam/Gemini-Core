# 📝 Gemini-Core: Operativ Tasklista

Denna lista hanterar de återstående stegen för att göra alla moduler 100% kompatibla med den nya Arkitektur v3.0.

## 🚀 Prioritet: Göra menyn "Meny-redo"
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
- [ ] **Systemoptimering**
    - [ ] Lägg till "Automisk Mirror" efter avslutade projektkörningar.
    - [ ] Skapa ett "Update All" kommando för Git-synk av alla sub-moduler.

## 🧠 Strategisk Utveckling
- [ ] **Dokumentations-audit**
    - [ ] Gå igenom alla `GEMINI.md`-filer (root och projekt) för att säkerställa att de matchar v3.0.
- [ ] **Core 4 Analys**
    - [ ] Se över hur vi använder "The 4 Core" (Project, Workspace, Shared, Skills) i praktiken.
- [ ] **Skills & Agents Setup**
    - [ ] Etablera strukturen för hur nya Skills skapas.
    - [ ] Definiera de första Agent-personorna i `Agents/`.
- [ ] **Workflow Definition**
    - [ ] Designa standard-workflowet för Gemini-Core (Planering -> Exekvering -> Spegling).

## ✅ Genomförda Milstolpar
- [x] Migrering till `C:\Gemini-Core`.
- [x] Etablering av privat GitHub-repo.
- [x] Implementering av `Mirror-Skill` (C: -> H:).
- [x] Skapat central hubb (`main.py`).
- [x] Konsolidering av projekt: Job-Hunter, Lego-Collector och Import-Engine flyttade till `Projects/`.
- [x] Aktiverat Mirror för alla projekt till Obsidian.
- [x] Arkiverat migrationsplanen till `Workspace/Archive`.
- [x] Uppdaterat speglings-mapping: Knowledge -> Skills.

---
*Senast uppdaterad: 2026-05-01*

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

## ✅ Genomförda Milstolpar
- [x] Migrering till `C:\Gemini-Core`.
- [x] Etablering av privat GitHub-repo.
- [x] Implementering av `Mirror-Skill` (C: -> H:).
- [x] Skapat central hubb (`main.py`).

---
*Senast uppdaterad: 2026-05-01*

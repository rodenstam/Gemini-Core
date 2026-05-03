---
id: citable-rag
version: 4.0
type: project
dependencies:
  - shared: gdrive_helper.py
  - shared: pdf_generator.py
stats:
  success_rate: 0.8
  last_run: 2026-05-01
---
# 📑 Project: Citable-RAG (Source-First Intelligence)

## Context
Detta projekt syftar till att bygga en anpassad RAG (Retrieval-Augmented Generation) optimerad för **utredningar**. Upplevelsen ska efterlikna NotebookLM: användaren ställer frågor till sitt källmaterial och sparar svar som strukturerade anteckningar i Obsidian. Systemet är en "sluten loop" där spårbarhet och bevisföring är högsta prioritet.

## Agent Mandates
1. **Strict Grounding:** LLM:en får ALDRIG gå utanför det tillhandahållna källmaterialet. Om svaret inte finns i källan ska den svara att information saknas.
2. **Source Integrity:** Varje genererat svar SKA innehålla källhänvisningar i Obsidian-kompatibelt format (t.ex. `[[Filnamn#page=X]]`).
3. **Investigation Workflow:** Systemet ska stödja ett flöde där svar kan konverteras till permanenta anteckningar med bibehållna källänkar.
4. **Anchor Points:** Vid indexering av dokument ska sidnummer och styckes-ID:n sparas som metadata.
5. **Color Awareness:** Systemet ska kunna prioritera text som användaren har highlightat (färgmarkerat) i originaldokumentet.

## Technical Strategy
- **Extraction:** Använd `PyMuPDF` för PDF-analys och `gdrive_helper.py` för åtkomst.
- **Linking:** Utnyttja Obsidian Deep Links för att hoppa direkt till rätt sida i PDF:er.
- **Portability:** Håll indexet kompakt och filbaserat (t.ex. JSON eller SQLite) för att fungera smidigt på Google Drive.

## Success Metrics
- [ ] Kan svara på en fråga och ange exakt sidnummer.
- [ ] Kan exportera en anteckning till Obsidian med fungerande länkar till källan.
- [ ] Kan läsa färgmarkeringar från en PDF på Drive.


# 🗺️ Roadmap: Citable-RAG

## Vision
Att skapa en personlig kunskapsmotor som aldrig tappar bort sina källor.

## Milestones

### Phase 1: Foundation (Current)
- [x] Projektstruktur och Core Four dokumentation.
- [ ] Research: Deep-linking i Obsidian (PDF-stöd).
- [ ] Research: Extrahera highlights och färger via PyMuPDF.

### Phase 2: The Ingestion Engine
- [ ] Skapa `ingestor.py` för att läsa Drive-filer.
- [ ] Implementera sid- och styckesindexering.
- [ ] Skapa en lokal vektordatabas (JSON/SQLite).

### Phase 3: The Query Engine
- [ ] Utveckla prompt-logik för att inkludera källhänvisningar i svaren.
- [ ] Integration med Gemini API.

### Phase 4: Obsidian Integration
- [ ] Export-funktion som skapar färdiga Markdown-filer med källhänvisningar.
- [ ] Automatisk länkning till originalet på Drive via "Digital Twin"-logik.

---
created: 2026-05-01
id: 2026-05-03-plan-semantic-search-integration
priority: medel
status: slutförd
tags: []
title: PLAN Semantic Search Integration (v1.1)
updated: '2026-05-03'
version: 1.0
---
# 🚀 PLAN: Semantic Search Integration (v1.1)

## 📋 Översikt
Detta initiativ syftar till att integrera semantisk sökning i Gemini-Core, inspirerat av "GenCLI". Målet är att göra hela kodbasen och dokumentationen sökbar baserat på betydelse (vektor-embeddings) snarare än bara nyckelord eller manifest-taggar.

## 🛠️ Arkitektur (Förslag)

### 1. Ny Skill: Skills/semantic-search
- **SKILL.md**: Manifest som definierar beroenden (Gemini API, numpy för likhetsberäkning).
- **engine.py**: Kärnlogik för:
  - Genomsökning av Projects/, Shared/ och docs/.
  - Hashing av filer för att upptäcka ändringar (effektivitet).
  - Generering av embeddings via Gemini API (text-embedding-004).
  - Lokal lagring av vektorer.
- **cli.py**: Ett enkelt gränssnitt för att ställa frågor som: "Hitta kodrelaterat till PDF-hantering".

### 2. Datalagring (Data/)
- **ile_hashes.json**: Lagrar senaste kända hash för varje indexerad fil.
- **ector_index.json**: Lagrar filbeskrivningar och deras motsvarande embeddings.

### 3. Agent-integration
- **Librarian**: Kan använda sökningen för att proaktivt föreslå relevant kontext när en ny uppgift påbörjas.
- **CLI Agent**: Kan använda sökningen för att snabbt navigera i okända delar av projektet.

## 📊 Rate Limit Strategi (Verifierad v4.2)
Se detaljerad referens i docs/GEMINI_API_RATE_LIMITS.md.
- **Indexering:** Vi använder **Gemini 3.1 Flash Lite** (Free Tier) för alla filbeskrivningar. Detta är den enda modellen med tillräcklig daglig kvot (500 RPD).
- **Vektorisering:** Använder text-embedding-004 (Free Tier) för sökvektorer (1500 RPM).

## 🎭 Dialectic Forum: Frågeställningar

### 🏛️ Arkitekten (Architect)
- Hur säkerställer vi att indexet inte blir för stort för att hanteras som en JSON-fil?
- Ska vi använda SQLite för att skala bättre?
- Hur hanterar vi temporära filer och .gitignore-mönster?

### 📚 Bibliotekarien (Librarian)
- Hur påverkar detta "Context Drift"? Kan vi använda sökresultat för att minska mängden data vi skickar till LLM:en?
- Hur ser vi till att sökresultaten är relevanta och inte bara "brus"?

### ⚡ Pragmatikern (Pragmatist)
- Kommer indexeringen ta för lång tid vid varje start?
- Hur minimerar vi antalet API-anrop till Gemini (kostnad/kvot)?
- Behöver vi verkligen en full vektor-sökning, eller räcker det med bättre manifest-indexering?

## 📅 Nästa Steg
1. **Aktivera Dialectic Forum**: Låt agenterna debattera förslaget.
2. **Prototyp**: Bygg en minimal version som bara indexerar Shared/.
3. **Validering**: Testa sökprecisionen på befintlig kod.

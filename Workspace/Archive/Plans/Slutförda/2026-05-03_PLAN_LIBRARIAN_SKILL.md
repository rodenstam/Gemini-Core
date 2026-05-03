---
created: 2026-05-03
id: 2026-05-03-plan-librarian-skill
priority: medel
status: slutförd
tags: []
title: DIALECTIC DEBATE Librarian Skill (v1.0)
updated: '2026-05-03'
version: 1.0
---
# 🎭 DIALECTIC DEBATE: Librarian Skill (v1.0)

**Datum**: 2026-05-03
**Ämne**: Implementering av `Skills/librarian` för systemomfattande ordning och reda.
**Deltagare**: 🏛️ Architect, ⚡ Pragmatist, 🚀 Visionary, 📚 Librarian.

---

## 🏛️ Fas 1: Positioner
*   **Architect** förespråkade strikt ordning och "Engineering Four"-standarden för att minska kognitiv belastning.
*   **Pragmatist** varnade för "process-overkill" och onödig byråkrati för små verktyg, samt kostnaden för semantisk sökning.
*   **Visionary** ville ha "Self-Healing" – automatisk flyttning av filer baserat på AI-analys.
*   **Librarian** betonade "findability" och behovet av att veta vad vi redan har gjort för att undvika dubbelarbete.

## ⚡ Fas 2: Granskning & Kritik
- **Architect -> Visionary**: "Automatisk flyttning är riskabelt för versionshantering (Git). Vi behöver spårbarhet."
- **Pragmatist -> Architect**: "Dina 'Engineering Four' är bra för stora projekt, men vi behöver en 'Lite-version' för små verktyg."
- **Librarian -> Visionary**: "Semantisk sökning är kraftfull, men vi måste vara försiktiga så att vi inte litar 100% på likhets-poäng."

## 🏛️ Fas 3: Syntes (vNext Förslag)
Efter debatten landade vi i:
1. **Dokumentations-Tiers**: Full (för projekt) och Lite (för verktyg).
2. **Safety-First (Migration Manifest)**: Librarian genererar förslag, användaren godkänner via `librarian apply`.
3. **Resurssnålhet**: Återanvändning av existerande semantiskt index.
4. **Ignore-system**: Stöd för `.librarian_ignore`.

---

# IMPLEMENTATION PLAN: Librarian Skill (v1.0)

## Objective
Create a "Librarian" skill that automates system organization, enforces documentation standards, and leverages semantic search for intelligent file management. This will transform the Librarian agent from a passive persona into an active automation tool.

## Key Files & Context
- **Root Directory**: `C:\Gemini-Core`
- **Skill Directory**: `Skills/librarian/`
- **Key Modules**:
    - `logic.py`: Core logic for auditing and organizing.
    - `rules.py`: System structure and file standards.
    - `cli.py`: User interface for triggering tasks.
- **Integration**: `main.py` (Central Hub).

## Proposed Solution

### 1. Structure Audit (Findability Engine)
The skill will scan all directories and compare them against the rules defined in `rules.py`.
- **Documentation Tiers**:
    - *Full*: Requires "Engineering Four" (DECISIONS, LOG, SPECS, TASKS) + `GEMINI.md` (for projects).
    - *Lite*: Requires only `GEMINI.md` or standardized file headers (for shared tools).
- **Plan Standards**: Plans in `Strategy/` must have YAML frontmatter:
    - `status`: (planerad | pågående | slutförd | avbruten)
    - `created`: YYYY-MM-DD
- **Ignore-System**: Support for `.librarian_ignore` to bypass specific folders (e.g., `Experimental/`).

### 2. Global Archiver & Migration Manifest
Extend the current `Shared/archiver.py` logic.
- **Chronological Archiving**: When a plan is archived, the librarian automatically prefixes it with its completion date (`YYYY-MM-DD_Filename.md`).
- **Migration Manifest**: Instead of moving files automatically, the librarian generates a JSON/Markdown manifest of suggested changes.
- **Command**: `librarian apply` executes the moves after user approval.

### 3. Semantic Sorting (Resource-Aware)
Utilize `Skills/semantic-search` efficiently:
- **Reuse Index**: Directly query `semantic_index.db` instead of generating new embeddings.
- Suggest moving files to the most relevant project folder based on vector similarity.

### 4. Stale Doc Detector
Analyze `last_indexed` or file metadata to identify documentation that hasn't been updated alongside related code changes.

## Phased Implementation Plan

### Phase 1: Foundation & Rules
- [x] Create `Skills/librarian/` directory and `SKILL.md`.
- [x] Implement `rules.py` with the Gemini-Core PARA/Manifest standards.
- [x] Implement a basic `audit` command in `cli.py`.

### Phase 2: Organization Logic
- [x] Implement `logic.py` with `audit_structure()` and `find_misplaced()`.
- [x] Implement a "Fix-it" mode that creates missing `GEMINI.md` skeletons or missing documentation files.
- [x] Port/Refactor `Shared/archiver.py` logic into `logic.py` for system-wide use.

### Phase 3: Semantic Integration
- [x] Create `semantic_helper.py` to interface with `Skills/semantic-search`.
- [x] Implement `suggest_location(file_path)` which uses vector similarity to find the best home for a file.
- [x] Implement redundant file detection.

### Phase 4: CLI Hub Integration
- [x] Update `main.py` to add "7. 📚 Librarian: System Tidy".
- [x] Add an interactive report showing all organization suggestions.

## Verification
1. **Audit Test**: Create a misplaced file in the root and verify that `librarian audit` detects it.
2. **Standardization Test**: Create a project without `LOG.md` and verify that the librarian can generate the missing file.
3. **Archive Test**: Successfully archive a test project from `Projects/` to `Workspace/Archive/`.
4. **Semantic Test**: Place a Lego-related text file in `Shared/` and verify that the librarian suggests moving it to `Projects/Lego-Collector/`.

## Migration and Rollback
- **Rollback**: Delete `Skills/librarian/` and remove the entry from `main.py`.
- **Migration**: Existing folders are not moved automatically without user confirmation in CLI mode.

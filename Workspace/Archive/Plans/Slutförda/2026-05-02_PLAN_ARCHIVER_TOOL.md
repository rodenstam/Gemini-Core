---
created: '2026-05-02'
id: 2026-05-02-plan-archiver-tool
priority: medel
status: planerad
tags: []
title: Plan Automated Archiver  Cleanup Tool (archiver.py)
updated: '2026-05-03'
version: 1.0
---
# 🗺️ Plan: Automated Archiver & Cleanup Tool (`archiver.py`)

**Status**: Draft / Strategy
**Target**: `Shared/archiver.py`

## 🎯 Goal
To automate the "Selective Archiving" protocol defined in `WORKFLOW.md`, ensuring that only high-value documents are preserved and the active workspace stays clean.

---

## 🏗️ Phase 1: Archiving Logic
- [ ] **Milestone Detection**: Identify completed `PLAN_*.md` files (all tasks checked).
- [ ] **Selective Packaging**: Create a subdirectory in `Archive/Plans/[Name]/`.
- [ ] **Transfer**: Move the plan and associated `DECISIONS.md` or major dialectics.

## 🛡️ Phase 2: Cleanup Logic
- [ ] **Temp File Detection**: Identify "floating" markdown files in `Strategy/` that aren't linked to an active plan.
- [ ] **User Confirmation**: Prompt the user before permanent deletion of non-essential materials.
- [ ] **Mirror Trigger**: Automatically run `mirror.py` after a successful cleanup.

## 🚀 Phase 3: CLI Integration
- [ ] **Command**: `python Shared/archiver.py --archive <plan_name>`
- [ ] **Status Report**: Provide a summary of what was saved and what was deleted.

---
*Created: 2026-05-02 | By: Gemini CLI Agent*

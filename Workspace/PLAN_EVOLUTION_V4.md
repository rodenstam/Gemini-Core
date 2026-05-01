# 🗺️ Implementation Plan: Gemini-Core v4.0 (The Hybrid Core)

**Status**: Proposal / Draft
**Target Version**: 4.0
**Reference Documents**: `Workspace/Strategy/DIALECTIC_FUTURE_EVOLUTION.md`, `Workspace/WORKFLOW.md`

## 🎯 Goal
To transition Gemini-Core from a file-based system with manual overhead to a **Manifest-Driven, Auto-Audited Hybrid System**. This ensures speed (Local Bus) without sacrificing durability (Markdown).

---

## 🏗️ Phase 1: Infrastructure & Manifests
*Upgrade all projects and skills to be "Self-Describing" and context-rich.*

- [ ] **Define Manifest Schema**: Standardize YAML frontmatter for all `GEMINI.md` and `SKILL.md` files.
    - Fields: `version`, `type` (project/skill/core), `dependencies` (list), `stats` (success_rate, last_run).
- [ ] **Batch Update & Content Refresh**: 
    - Inject YAML manifests into all root and project-level `GEMINI.md` files.
    - **Content Audit**: Update the actual descriptive content in `GEMINI.md` files to ensure they reflect the current architecture and agent mandates (v4.0 standards).
- [ ] **Update WORKFLOW.md**: Formally include the "Manifest-First" rule and activation logic.

## 🛡️ Phase 2: The System Guard (Shared Auditor)
*Ensure the auditor is robust and functional before moving to active enforcement.*

- [ ] **Auditor Stabilization**: Refactor `Experimental/core_auditor.py` to handle errors gracefully, support the new YAML schema, and ensure it provides clear, actionable feedback.
- [ ] **Relocate**: Move stabilized code to `Shared/auditor.py`.
- [ ] **Feature Upgrade**:
    - Validate YAML manifests against the schema.
    - Generate `Data/dependency_graph.json`.
    - Detect "Zombie Projects" (no activity > 60 days).
- [ ] **Integration**: Add `python Shared/auditor.py` as a recommended (but not always mandatory) step in the "Phase-End" workflow.

## ⚡ Phase 3: The Local State Bus (Efficiency)
*Reduce context overhead by storing volatile data outside of Markdown.*

- [ ] **Initialize**: Create `Data/session_state.json`.
- [ ] **Agent Integration**: Update agent mandates to use this file for:
    - Tracking the current active Phase/Task.
    - Storing transient variable values.
    - Error-loop counters (to trigger architectural re-evaluation).

## 🚀 Phase 4: Workflow Activation & UX
*Ensure the system remains flexible and non-intrusive.*

- [ ] **Brainstorm-to-Workflow Transition**: Implement a standard "Gate" where the agent, after a brainstorming phase, explicitly asks: *"Should we proceed with the Gemini-Core Workflow (Adaptive Planning) for this task?"*
- [ ] **Optionality Protocol**: Define scenarios where the formal workflow is skipped (e.g., quick queries, non-code changes) to maintain "Flow State".
- [ ] **Terminal Reset Recommendation**: After significant system updates (like this v4.0 migration), the agent should recommend: *"System state has changed significantly. Consider closing this terminal and restarting with `gemini -y` to ensure a clean context."*

## 🔄 Phase 5: Atomic Background Mirroring
*Decouple the UI (Obsidian) from the Engine (CLI).*

- [ ] **Refactor Mirror-Skill**: Implement a "Stage-and-Swap" directory strategy.
- [ ] **Background Execution**: Create a lightweight watcher or ensure `mirror.py` runs asynchronously at the end of every successful `auditor.py` run.
- [ ] **Visual Feedback**: Add a "Mirror Status" badge to the Obsidian dashboard (via a generated `MIRROR_STATUS.md`).

---

## 📈 Success Metrics
1. **Zero Broken Links**: Auditor confirms all dependency paths exist.
2. **Reduced Latency**: Agents use `session_state.json` instead of re-reading large `tasks.md` files for simple status checks.
3. **Consistency**: 100% of projects follow the Manifest Schema.

---
*Created: 2026-05-01 | By: Gemini CLI Agent*

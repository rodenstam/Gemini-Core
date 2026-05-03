---
id: gemini-core
version: 4.3
type: core
dependencies:
  - skill: mirror
  - skill: semantic-search
  - skill: workflow
  - shared: auditor.py
stats:
  success_rate: 1.0
  last_run: 2026-05-03
---
# 🏛️ Gemini Core: Master Context (v4.3)

Detta är det centrala operativsystemet för AI-automation. Systemet drivs av en **Manifest-Driven arkitektur** (v4.3) med ett utökat **Agent-Modulärt bibliotek**, **Semantisk sökning** och ett **Expert-Arbetsflöde**.

## ⚡️ Driftläge: YOLO (Autonomous Mode)
1. **Local Bus Execution**: All kod och logik körs från `C:\Gemini-Core`. Volatil data lagras i `Data/session_state.json`.
2. **Professional Setup**: Separera exekvering (C:) från presentation (H:).
3. **Manifest-Driven Lifecycle**: Alla projekt och skills styrs av YAML-manifest som uppdateras både FÖRE och EFTER genomförande.
4. **Semantiskt Minne**: Systemet använder `Skills/semantic-search` för att ge agenter tillgång till hela kodbasens kontext via vektor-embeddings.
5. **Agent-Modulär Struktur**: Vi använder ett bibliotek av specialiserade agenter (`Agents/`) som kan kombineras i Dialectic Forums.

## 📂 Systemstruktur (C:\Gemini-Core)
- **`Workspace/`**: Planering och arkitektur.
    - `Strategy/`: Kladd och tillfälligt material för planer under framtagande.
    - `Plans/`: Aktiva planer under genomförande (`Planerade/`, `Pågående/`).
    - `Archive/`: Slutförda eller avbrutna planer i ren filform.
- **`Projects/`**: Aktiva projekt. Varje projekt är "Self-Describing" via sitt manifest.
- **`Skills/`**: Modulära AI-förmågor (inklusive `workflow`).
- **`Shared/`**: Globala Python-verktyg.
- **`Data/`**: Systemets minne (Credentials & Session State).
- **`docs/`**: Teknisk systemdokumentation.

## 🪞 Speglings-mappning (C: -> H:)
- `Workspace/` -> `Management/`
- `Projects/` -> `Projects/`
- `Skills/` -> `Skills/`
- `docs/` -> `System/docs/`
- Root `.md` -> Root

## 📜 Regler & Mandat
- **Manifest-Lifecycle**: Manifest SKALL uppdateras i början (för planering) och i slutet (för att säkra resultatet) av varje uppgift.
- **Workflow Skill Activation**: Aktivera `Skills/workflow` vid varje ny huvuduppgift för att säkerställa metodik.
- **Librarian Enforcement**: Använd `Skills/librarian` för att automatisera flytt av planer och arkivering.
- **Auto-Mirror Mandate**: Efter ändringar i Markdown SKALL `python Skills/mirror/mirror.py` köras.
- **Local State Bus**: Använd `Data/session_state.json` för att spåra aktuell fas och minska context bloat.

---
*Senast uppdaterad: 2026-05-03 (Librarian & Workflow Update)*

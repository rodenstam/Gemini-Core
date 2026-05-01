# 🛡️ PROPOSAL: Workflow Enforcement (The Guardrails)

Hur säkerställer vi att vi faktiskt följer "Brainstorm -> Plan -> Execute -> Review"?

## 1. Mekaniken: `ACTIVE_PLAN.md`
För varje större uppgift skapas en `Workspace/ACTIVE_PLAN.md` (eller ett unikt namn). Denna fil fungerar som en "Gater":
*   **Checkpoint-Gating**: Jag (AI:n) får inte radera eller markera en fas som klar utan att bifoga en `VALIDATION_NOTE` i samma fil.
*   **Human-Check**: Innan jag går från en fas (t.ex. Planering) till nästa (Execution), måste jag explicit fråga: *"Planen är klar i ACTIVE_PLAN.md. Ska vi aktivera 'gemini -y' för Fas 1?"*

## 2. Agent-Personor (Roles)
Vi använder specifika instruktions-filer i `Agents/` för att styra mitt beteende:
*   **`Agents/architect.md`**: Aktiveras under Brainstorm & Plan. Fokus på att "tänka utanför boxen" och hitta brister i logiken.
*   **`Agents/developer.md`**: Aktiveras under Execution. Fokus på ren kod, prestanda och verifiering.

## 3. Mirror som "Proof of Work"
*   Genom att köra `Mirror-Skill` efter varje avslutad fas blir mina framsteg synliga i Obsidian.
*   Detta ger dig möjligheten att granska arbetet asynkront (t.ex. på mobilen) och ge feedback i nästa session.

## 4. Session-Persistence (Återstart)
Varje ny session inleds med:
1.  Läsa `Workspace/tasks.md` (Vad ska göras?).
2.  Läsa `Workspace/ACTIVE_PLAN.md` (Var är vi i detalj?).
3.  Ge en kort status-uppdatering till användaren.

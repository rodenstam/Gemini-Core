---
created: '2026-05-03'
id: 2026-05-03-plan-plan-reorganization
priority: hög
status: slutförd
tags:
- arkitektur
- librarian
- refactoring
title: Plan för omorganisation av planer och arkiv
updated: '2026-05-03'
version: 1.0
---
# Plan för omorganisation av planer och arkiv

## Bakgrund & Syfte
Efter diskussion har vi insett att det behövs en dedikerad plats för "kladd" och tillfälligt arbetsmaterial (debatter, utkast, loggar) medan en plan tas fram. När planen väl är färdig och godkänd ska den flyttas till en tydlig struktur för aktiva planer, och slutligen arkiveras som en enda fil utan extra kringmaterial.

Syftet med denna omorganisation är att:
1. Skapa en tydlig livscykel för planer: Utkast -> Aktiv -> Arkiverad.
2. Använda `Workspace/Strategy/` som den kreativa ytan (för material och utkast).
3. Införa `Workspace/Plans/` för aktiva planer (planerade och pågående).
4. Eliminera undermappar för milstolpar i arkivet. Vid arkivering rensas arbetsmaterial bort och eventuell viktig information summeras in i huvudplanen (En plan = en fil).

## Målstruktur

### 1. Utkast & Arbetsmaterial
* **`Workspace/Strategy/`**
  Här skapas filerna från början. Här får man ha hur många filer man vill (debatter, resultat, loggar) medan planen tas fram.

### 2. Aktiva Planer
När en plan är färdigutvecklad och redo att utföras flyttas själva plan-filen hit. Tillfälligt arbetsmaterial raderas eller sammanfattas i planen.
* **`Workspace/Plans/Planerade/`** - Planer som är godkända men inte påbörjade (status `planerad`).
* **`Workspace/Plans/Pågående/`** - Planer som aktivt genomförs (status `pågående`).

### 3. Arkiverade Planer
När en plan är klar flyttas den hit. Fortfarande gäller regeln: En plan = en fil.
* **`Workspace/Archive/Plans/Slutförda/`** - (status `slutförd`).
* **`Workspace/Archive/Plans/Avbrutna/`** - (status `avbruten`).

## Steg för genomförande

### Fas 1: Konsolidering av befintliga filer
*   **System_Integrity_Debate:** Slå ihop `2026-05-02_INTEGRITY_DEBATE_RESULTS.md` in i `2026-05-02_PLAN_SYSTEM_INTEGRITY_DEBATE.md`.
*   **v4_Migration:** Slå ihop `DIALECTIC_FUTURE_EVOLUTION.md`, `DECISIONS.md`, och `LOG.md` in i `2026-05-01_PLAN_EVOLUTION_V4.md`.
*   Alla arkiverade planer flyttas till `Workspace/Archive/Plans/Slutförda/`. Milstolpsmapparna raderas.

### Fas 2: Uppdatering av Librarian (Skill)
1.  **`rules.py`**:
    *   `STRATEGY_DIR` ändras till att övervaka `Workspace/Strategy` (för utkast), samt lägga till `ACTIVE_PLANS_DIRS` (`Workspace/Plans/Planerade`, `Workspace/Plans/Pågående`).
2.  **`cli.py`**:
    *   Kommandot `archive` uppdateras till att bara ta ett argument (plan-filen) och automatiskt flytta den till `Slutförda` eller `Avbrutna` baserat på YAML.
3.  **`logic.py`**:
    *   `audit_plans` övervakar nu både `Workspace/Strategy/` och `Workspace/Plans/`.
    *   `audit_archive` säkerställer att inga undermappar finns förutom `Slutförda/` och `Avbrutna/`.

### Fas 3: Strukturmigrering och Tidy
1. Skapa de nya mapparna i `Workspace/`.
2. Flytta existerande planer som är pågående till `Workspace/Plans/Pågående/`.
3. Kör `python Skills/librarian/cli.py tidy` för att verifiera allt.

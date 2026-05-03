---
created: '2026-05-03'
id: plan-yaml-standard-v1
priority: hög
status: slutförd
tags:
- arkitektur
- standard
- yaml
- debatt
title: 'PROPOSAL: Gemini-Core YAML Standard v1.0'
updated: '2026-05-03'
version: 1.0
---
# 📜 PROPOSAL: Gemini-Core YAML Standard v1.0

## 🎯 Syfte
Att definiera ett enhetligt system för metadata som gör Gemini-Core maskinläsbart, spårbart och automatiserat, utan att skapa onödig administrativ börda.

## 🏗️ Föreslagen Arkitektur

### 1. Modul-ID & Arv
Varje huvudmanifest (`GEMINI.md` eller `SKILL.md`) ska ha ett unikt `id`. Allt innehåll i manifestets mapp (och undermappar) anses tillhöra detta ID.
*   **Fördel**: Vi slipper skriva YAML i varje enskild fil.
*   **Logik**: Om en fil ligger i `Projects/Citable-RAG/docs/LOG.md`, är dess "ägare" det projekt som har manifestet i `Projects/Citable-RAG/`.

### 2. Standardfält (The Core Set)
Alla manifest SKALL innehålla:
*   **`id`**: Kebab-case (t.ex. `citable-rag`).
*   **`version`**: Semantisk versionering för modulen.
*   **`type`**: `core`, `project`, `skill` eller `plan`.
*   **`status`**: (Speciellt för planer) `utkast`, `planerad`, `pågående`, `slutförd`, `avbruten`.

### 3. Utökade fält (The Intelligence Set)
Fält som hjälper CLI-agenten och Librarian:
*   **`category`**: Hjälper Librarian att kategorisera projekt (t.ex. `rag`, `automation`, `research`).
*   **`priority`**: `låg`, `medel`, `hög`.
*   **`owner`**: Vem (vilken agent eller användare) som ansvarar för modulen.

### 4. Koppling av "Lösa Filer"
För filer som inte ligger i en tydlig modul-mapp (t.ex. i `Shared/`):
*   Manifestet kan ha ett fält `exports` som listar filer som modulen tillhandahåller.
*   Alternativt kan `auditor.py` skanna efter beroenden och bygga kopplingen automatiskt i `Data/dependency_graph.json`.

---

## 🏛️ Syntes: Den förfinade standarden (v1.0)

Efter Dialectic Forum har vi landat i följande kompromiss som balanserar ordning med enkelhet:

### 1. Obligatoriskt `id` (Primary Key)
*   **Regel**: Varje `GEMINI.md` och `SKILL.md` SKALL ha ett unikt `id`-fält.
*   **Varför**: Detta frikopplar projektets identitet från dess mappnamn. Om vi flyttar en mapp (t.ex. till arkivet) förblir alla referenser i databaser och beroendegrafen intakta.
*   **Enforcement**: `auditor.py` kommer varna om `id` och mappnamn skiljer sig åt för att undvika förvirring, men systemet tillåter det.

### 2. Namespace Inheritance (Crawl-Up)
*   **Regel**: Inga YAML-headers krävs i undermappar som `docs/` eller `engine/`.
*   **Logik**: Agenter och verktyg (Librarian/Auditor) använder en "Crawl-Up"-algoritm. Om en fil saknar manifest letar systemet uppåt i mappträdet tills det hittar närmaste `GEMINI.md` eller `SKILL.md`. Den filen anses då vara "ägaren".
*   **Orphan Detection**: `auditor.py` kommer att flagga filer som inte kan kopplas till något manifest som "föräldralösa".

### 3. Maskinläsbara Status-övergångar
*   **Regel**: Planer SKALL använda status-fältet för att styra automatisering.
*   **Trigger**: När status ändras till `pågående` eller `slutförd` kör CLI-agenten automatiskt `librarian fix` för att flytta filen till rätt fysisk plats.

---

## 🚀 Implementeringssteg

### Fas 1: Uppdatera Verktyg
1.  [x] **`Shared/auditor.py`**: Uppdatera för att stödja `id`-validering och Crawl-Up logik.
2.  [x] **`Skills/librarian/logic.py`**: Uppdatera för att använda `id` vid indexering snarare än bara sökvägar.

### Fas 2: Standardisering av existerande manifest
1.  [x] Lägg till `id` i root-manifestet.
2.  [x] Lägg till `id` i alla projekt (`Citable-RAG`, `Job-Hunter-CLI`, etc.).
3.  [x] Lägg till `id` i alla skills.

### Fas 3: Verifiering
1.  [x] Kör en fullständig system-audit för att se att inga filer är föräldralösa.
2.  [x] Verifiera att semantisk sökning kan gruppera filer baserat på ID.

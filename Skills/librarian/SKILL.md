---
id: librarian
version: 1.0
type: skill
description: Automatiserad systemordning, dokumentationskontroll och intelligent arkivering.
dependencies:
  - skill: semantic-search
  - shared: auditor.py
---
# 📚 Skill: Librarian

Håller Gemini-Core organiserat genom att granska filstruktur, genomdriva dokumentationsstandarder och föreslå intelligenta flyttar av filer.

## 🛠️ Funktioner
1.  **System Audit:** Kontrollerar att alla projekt och skills följer rätt mappstruktur och har nödvändig dokumentation.
2.  **Plan Tracking:** Bevakar status på planer i `Strategy/` och säkerställer att de arkiveras korrekt med datumstämpel.
3.  **Intelligent Sortering:** Använder semantisk sökning för att föreslå var lösa filer bäst hör hemma.
4.  **Migration Manifest:** Genererar förslag på ändringar som användaren kan godkänna innan de genomförs.

## 🚀 Kommandon

### Granska systemet
Hittar felaktigt placerade filer eller saknad dokumentation.
```bash
python Skills/librarian/cli.py audit
```

### Arkivera en plan
Flyttar en slutförd plan till arkivet och döper om den kronologiskt.
```bash
python Skills/librarian/cli.py archive <plan_fil> <milestone_namn>
```

### Städa systemet (Tidy)
Kör en fullständig genomgång och föreslår optimeringar.
```bash
python Skills/librarian/cli.py tidy
```

## 🤖 För Agenter
Librarian kan användas för att validera en arbetsyta innan en uppgift påbörjas eller avslutas.

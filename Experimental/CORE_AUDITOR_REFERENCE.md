# 🛡️ Core Auditor: Systemöversikt

Core Auditor är Gemini Cores interna arkitekturväktare. Dess syfte är att säkerställa att systemet förblir snabbt, korrekt och välorganiserat även när antalet projekt växer.

## 🛠️ Nuvarande Kapacitet (v0.1)
I sin nuvarande form utför auditorn följande kontroller:

1.  **Struktur-validering:** Kontrollerar att varje projektmapp har en `docs/`-undermapp.
2.  **The Core Four Check:** Verifierar att de obligatoriska dokumenten (`tasks.md`, `pins.md`, `devlog.md`, `roadmap.md`) existerar.
3.  **Länk-integritet:** Scannar `GEMINI.md`-filer efter Python-kommandon och validerar att de pekar på faktiska filer i `Engine/`.
4.  **Inaktivitets-analys (Staleness):** Flaggar projekt som inte har uppdaterats på 30 dagar (baserat på `devlog.md`).

## 🚀 Användning (Under utveckling)
Körs manuellt via terminalen (lokalt på C:):
```powershell
python "C:\Gemini-Core\Experimental\core_auditor.py"
```

## 📈 Utvecklingsplan (Roadmap)

### Fas 1: Automatiserad Stöd (Inom kort)
- [ ] **Mallsystem:** Lägg till en `--fix` flagga som skapar saknade `docs/`-filer utifrån standardmallar.
- [ ] **Context Audit:** Varna om en `GEMINI.md` fil är för stor (>2000 ord) och föreslå uppdelning.

### Fas 2: Intelligens & Optimering
- [ ] **Dependency Mapping:** Analysera vilka `Engine/Shared`-skript som används av flest projekt för att identifiera kandidater för "Core Library".
- [ ] **Skill Conversion:** Identifiera projekt som med fördel kan konverteras till en "Skill" för att spara uppstartstid.

### Fas 3: Självläkning
- [ ] **Auto-Archive:** Föreslå flytt av inaktiva projekt till en arkiv-mapp för att hålla Obsidian-vyn ren.
- [ ] **Path Repair:** Identifiera flyttade skript i `Engine/` och uppdatera länkarna i projektens `GEMINI.md` automatiskt.

---
*Senast uppdaterad: 2026-04-29 | Status: Operativ (v0.1)*

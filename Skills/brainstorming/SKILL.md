---
version: 4.0
type: skill
dependencies: []
stats:
  success_rate: 1.0
  last_run: 2026-05-01
---
# 🧠 Skill: Brainstorming
**Syfte**: Att förvandla diffusa idéer till tekniska specifikationer innan kodning påbörjas.

## 🛠️ Process
1. **Frågestadiet**: Ställ frågor till användaren för att förstå målet, begränsningar och önskat resultat.
2. **Utforskning (Dialectic Mode)**: Vid komplexa beslut, aktivera ett **Dialectic Forum** enligt `Agents/DIALECTIC_PROTOCOL.md`. Använd relevanta agenter (t.ex. Architect + Pragmatist + Auditor) för att debattera lösningen.
3. **Validering**: Presentera en sammanfattning av den valda designen i korta stycken för användaren att godkänna.

## 📋 Regler
- Skriv aldrig kod under brainstorming-fasen.
- Använd Markdown-tabeller för att jämföra alternativ.
- Spara det slutgiltiga beslutet i `docs/designs/`.


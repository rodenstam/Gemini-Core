# 🪞 Skill: Mirror
**Syfte**: Att automatiskt spegla operativ dokumentation från den lokala arbetsytan (`C:`) till Obsidian (`H:`) för en ren och tillgänglig läsvy.

## 🛠️ Process
1. **Identifiering**: Skillen bevakar eller skannar mappar som `Workspace/`, `Projects/` och `Skills/`.
2. **Filtrering**: Endast relevanta läsfiler speglas (`.md`, `.pdf`, `.png`). Kod och tekniska filer exkluderas.
3. **Mappning**: Lokala mappar översätts till en logisk struktur i Obsidian:
   - `Workspace/` -> `Management/`
   - `Projects/` -> `Projects/`
   - `Skills/` -> `Knowledge/`

## 📋 Regler
- **Enkelriktad**: Spegling sker alltid från `C:` till `H:`. Ändringar i Obsidian skrivs över vid nästa synk.
- **On-demand**: Körs manuellt eller triggas av andra agenter efter att de skapat/ändrat dokumentation.
- **Säkerhet**: Speglar aldrig `.env` eller filer i `Data/Credentials/`.

# 🏛️ Gemini Core: Master Context (v3.0)

Detta är det övergripande operativsystemet för all AI-automation. Systemet är nu migrerat till en lokal arkitektur på `C:\Gemini-Core` för exekvering, med spegling till Obsidian-valvet på Google Drive (`H:\My Drive\Obsidian`).

## ⚡️ Driftläge: YOLO (Autonomous Mode)
1. **Local Execution**: All kod och logik körs från `C:\Gemini-Core`.
2. **Professional Setup**: Separera exekvering (C:) från presentation (H:).
3. **Mirror-Logic**: All operativ dokumentation speglas automatiskt från `C:` till `H:` via `Mirror-Skill`.
4. **Agentisk Struktur**: Vi använder "Skills" (instruktioner) och "Agents" (personor) för att styra AI-arbetet.

## 📂 Systemstruktur (C:\Gemini-Core)
- **`Workspace/`**: Övergripande planering och arkitektur (Speglar till `Management/` i Obsidian).
- **`Projects/`**: Aktiva projekt (t.ex. Job-Hunter, Lego-Collector). Varje projekt har sin egen kod och `docs/`.
- **`Skills/`**: Modulära AI-förmågor (t.ex. `mirror`, `brainstorming`). (Speglar till `Skills/` i Obsidian).
- **`Shared/`**: Globala Python-verktyg och hjälpare.
- **`Data/`**: Systemets minne (Credentials & Register). **Ignoreras av Git.**
- **`docs/`**: Teknisk systemdokumentation. (Speglar till `System/docs/` i Obsidian).

## 🪞 Speglings-mappning (C: -> H:)
Systemet använder `Skills/mirror/mirror.py` för att hålla Obsidian uppdaterat:
- `Workspace/` -> `Management/`
- `Projects/` -> `Projects/`
- `Skills/` -> `Skills/`
- `docs/` -> `System/docs/`
- Root `.md` -> Root

## 📜 Regler & Mandat
- **Sanningen på C:** Alla ändringar i dokumentation SKALL ske på `C:\Gemini-Core`. Obsidian-vyn på `H:` är endast för läsning.
- **Auto-Mirror**: Efter att ha skapat eller ändrat en Markdown-fil som ska vara synlig i Obsidian, KÖR `python Skills/mirror/mirror.py`.
- **Git First**: Alla kodändringar ska commitas till det privata GitHub-repot.
- **Säkerhet**: Spegla ALDRIG filer i `Data/Credentials/` eller `.env`.

---
*Senast uppdaterad: 2026-05-01 (Mirror-Skill implementerad)*

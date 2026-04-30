# ✅ Att-göra: LEGO Collector

Denna fil innehåller uppgifter och status för LEGO Collector-projektet.

---

## Aktuella Uppgifter
- [ ] **Förbättringar & Underhåll**
    - [ ] Skapa ett migrations-skript ifall metadata-schemat ändras i framtiden.
- [ ] **Notion-koppling**
    - [ ] Dokumentera hur man bäst importerar de genererade `.md`-filerna till en Notion-databas.
    - [ ] Undersök om vi kan använda Notions API för att synka direkt utan manuell import.
- [ ] **Dashboard Utökning**
    - [ ] Lägg till en tabellvy som alternativ till gallerivyn.
    - [ ] Implementera en knapp för att trigga synk direkt från webbsidan? (Kräver en liten backend-server).

---

## Slutförda Uppgifter

- [x] **Samlingshantering & Synk (NY!)**
    - [x] Implementerat `--own` och `--want` för att uppdatera Brickset direkt från CLI.
    - [x] Implementerat `--import_file` för bulk-import från textfil.
    - [x] Skapat smart sortering i `collection_list.txt` (automatisk flytt till SYNCED-sektion).
    - [x] Säkerställt att "Owned"-status alltid synkas vid import oavsett om filen finns lokalt.
- [x] **Initiering och Projektstruktur**
    - [x] Skapat projektmappen `/projects/Lego_Collector/`.
    - [x] Skapat `brickset_tool.py` och `config.py`.
    - [x] Skapat `.env` mall för API-nycklar.
    - [x] Skapat mappar för `/sets/` och `/sets/images/`.
- [x] **API-integration & Datahämtning**
    - [x] Implementerat `get_user_hash()` för inloggning.
    - [x] Implementerat `fetch_set_data()` med `getSets` API v3.
    - [x] Implementerat automatisk hantering av `-1` suffix för set-nummer.
    - [x] Implementerat bildhämtning och lokal bildlagring.
- [x] **Metadata & Notion-anpassning**
    - [x] Skapat YAML Frontmatter med fält för `namn`, `id`, `setID`, `skick`, `Kategori`, `Tema`, `delar`, `Released`, `minifigures`, `byggat`.
    - [x] Implementerat stöd för CLI-flaggor (`--skick`, `--byggat`).
- [x] **Visuell Dashboard**
    - [x] Skapat `dashboard.html` med modern grid-vy.
    - [x] Skapat `sets_data.js` för dynamisk inläsning av data.

# 📊 Gemini API: Rate Limits (Verifierade Maj 2026)

Detta dokument innehåller de EXAKTA rate limits som gäller för dina AI Studio-nycklar (Free & Paid). Dessa siffror går före alla generella sökningar.

## 🆓 Free Tier (Verifierad Dashboard)
*Används för bakgrundsarbete och mass-indexering.*

| Modell | RPM (Req/Min) | TPM (Tokens/Min) | RPD (Req/Day) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 3.1 Flash Lite** | 15 | 250 000 | 500 | **Bäst för mass-indexering** |
| **Gemini 3 Flash** | 5 | 250 000 | 20 | Begränsad |
| **Gemini 2.5 Flash** | 5 | 250 000 | 20 | Begränsad |
| **Gemini 2.5 Flash Lite** | 10 | 250 000 | 20 | Begränsad |

---

## 💰 Paid Tier (Verifierad Dashboard)
*Används för realtids-sökningar och vid behov av obegränsad kapacitet.*

| Modell | RPM (Req/Min) | TPM (Tokens/Min) | RPD (Req/Day) |
| :--- | :--- | :--- | :--- |
| **Gemini 2 Flash** | 2 000 | 4 000 000 | **Unlimited** |
| **Gemini 2.5 Flash Lite** | 4 000 | 4 000 000 | **Unlimited** |
| **Gemini 3.1 Flash Lite** | 4 000 | 4 000 000 | 150 000 |
| **Gemini 3 Flash** | 1 000 | 2 000 000 | 10 000 |
| **Gemini 2.5 Flash** | 1 000 | 1 000 000 | 10 000 |
| **Gemini 2.5 Pro** | 150 | 2 000 000 | 1 000 |
| **Gemini 3.1 Pro** | 25 | 2 000 000 | 250 |

---

## 🛠️ Hybrid-Strategi för Gemini-Core

1.  **Indexering (Free Tier First):** Vi börjar alltid med **Gemini 3.1 Flash Lite** på Free Tier för att förbruka de 500 gratis-anropen först.
2.  **Överspill (Paid Tier):** Om vi behöver indexera mer än 500 filer på en dag, växlar systemet automatiskt till **Gemini 2.5 Flash Lite** på Paid Tier, som har **Unlimited RPD**.
3.  **Sökning:** Vi använder 	ext-embedding-004 (Free Tier) för sökvektorer.
4.  **Resonemang (Paid Tier):** För komplexa svar använder vi **Gemini 2.5 Pro** eller **3.1 Pro** beroende på tillgänglig kvot.

---
*Källa: Användarens AI Studio Dashboard (Maj 2026)*

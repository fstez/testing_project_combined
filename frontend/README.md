# Frontend – A/B katse demo

## Kiirstart
```bash
cd /Users/robinrattasep/testing_project/frontend
python -m http.server 4173
```
Seejärel ava brauseris `http://localhost:4173`.

## Põhikomponendid
- `index.html` – staatiline leht koos GA4 sildiga ja andmesektsiooniga.
- `style.css` – minimalistlik kujundus, et variandid eristuksid.
- `ab.js` – A/B loogika (variandi valik, sündmused, HTML genereerimine).
- `app.js` – DOM sündmused, backend andmete päring, GA sündmuste vallandamine.

## Arendusvihjed
- Asenda `G-XXXXTEST` oma mõõtmistunnusega või kasuta `.env` injektsiooni.
- Hoia backend vaikimisi aadressil `http://localhost:8000`; vajadusel kasuta `window.API_URL`.
- Lisa uued variandid `ab.js` massiivi `VARIANDID`, et testid neid automaatselt haaraksid.


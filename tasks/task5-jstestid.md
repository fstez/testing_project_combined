# Task 5 – JavaScript testid

**Kestus:** ~15 min

## Info (20%)
Jest võimaldab A/B loogikat testida Node'i keskkonnas ilma brauserita, kontrollides nii variandi valikut kui ka sündmuste atribuute.

## Ülesanne (60%)
- Kirjuta `tests-js/` alla vähemalt neli testi `frontend/ab.js` funktsioonidele (variandi valik, vahetus, sündmuse keha, salvestamine).
- Mocki `localStorage` lihtsa objektiga ja kinnita fallback-loogika.
- Käivita `cd tests-js && npm install && npm test`, salvesta logi `docs/results/jest/jest.log` ja viita testiplaanis.

## Valmisoleku kontroll (20%)
- `npm test` jookseb roheliselt ja logi on `docs/results/jest/`.
- Vähemalt üks test kontrollib GA metaandmeid ning töö kirjeldus lisatud `docs/testplan.md`.

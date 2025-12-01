# Task 6 – A/B testimine

**Kestus:** ~15 min

## Info (20%)
A/B eksperiment võrdleb kahte kasutajaliidest. Variandi valik, salvestus ja sündmuste logimine peavad olema jälgitavad, et hiljem mõõta tulemusi ja valideerida testidega.

## Ülesanne (60%)
- Täienda `frontend/ab.js`, et mõlemad variandid oleksid selgelt eristatavad ning funktsioonid `valiVariant`, `vahetaVariant`, `looLayoutHTML` käituksid deterministlikult.
- Lisa `frontend/app.js` faili nupp variandi vahetamiseks, salvesta eelistus `localStorage`-s ja vallanda sündmused `variant_vaade` + `variant_vahetus`.
- Kirjelda `docs/testplan.md` failis mõõdikud ja minimaalse prooviaja plaan; salvesta logiviited `docs/results/analytics/`.

## Valmisoleku kontroll (20%)
- Mõlemal variandil on unikaalne klass/atribuut ning need ilmuvad GA sündmustes.
- `localStorage` säilitab valiku; JS testid katavad loogika ja viide lisatud `docs/testplan.md`.

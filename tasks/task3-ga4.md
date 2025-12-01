# Task 3 – Google Analytics GA4 integreerimine

**Kestus:** ~15 min

## Info (20%)
GA4 jälgib kasutaja tegevusi sündmustena. Vajad mõõtmistunnust, `gtag.js` skripti ja sündmuste käsitlemist, et A/B test oleks mõõdetav.

## Ülesanne (60%)
- Käivita frontend `cd frontend && python -m http.server 4173`.
- Lisa `frontend/index.html` faili GA4 skript mõõtmistunnusega (mock `G-XXXXTEST` sobib arenduses).
- Kutsu `gtag('event', 'variant_vaade', {...})` ja `gtag('event', 'variant_vahetus', {...})` iga layout'i muudatuse korral.
- Salvesta võrgu- või DebugView ekraanipildid `docs/results/analytics/` kausta ja lisa need **selle faili lõppu** Markdown-piltidena (nt `![GA4](../docs/results/analytics/ga4.png)`).

## Valmisoleku kontroll (20%)
- Brauseri võrgupaneel näitab GA4 päringut sündmusega, mis sisaldab `variant`, `sessioonId`, `katsestaadium`.
- Ekraanipildid on nii `docs/results/analytics/` kaustas kui ka lisatud siia faili.

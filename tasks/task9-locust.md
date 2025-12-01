# Task 9 – Locust koormustest

**Kestus:** ~15 min

## Info (20%)
Locust kirjeldab kasutaja käitumist Pythonis. Sellega saad hinnata, kuidas backend reageerib 20–50 samaaegsele kasutajale ning kas API-de latentsus püsib aktsepteeritud piirides.

## Ülesanne (60%)
- Veendu, et backend töötab: `uvicorn backend.main:rakendus --reload`.
- macOS/Linux: `source .venv/bin/activate && locust -f tests-performance-locust/locustfile.py --headless -u 50 -r 5 --run-time 5m --host http://localhost:8000 --csv docs/results/locust/koormus`; Windows PowerShell: `.\.venv\Scripts\Activate.ps1; locust -f tests-performance-locust/locustfile.py --headless -u 50 -r 5 --run-time 5m --host http://localhost:8000 --csv docs/results/locust/koormus`.
- Analüüsi väljundit (läbilaskevõime, p95 latentsus, veaprotsent), salvesta aruanded `docs/results/locust/`.
- Tee tulemustest ekraanipildid ja lisa need nii `docs/results/locust/` kausta kui ka **selle faili lõppu** Markdown-piltidena (nt `![Locust](../docs/results/locust/koormus.png)`).

## Valmisoleku kontroll (20%)
- Käsurea parameetrid on dokumenteeritud ja CSV/HTML failid paiknevad `docs/results/locust/`.
- Ekraanipildid on imporditud selle faili lõppu ning riskianalüüs uuendatud `docs/testplan.md` dokumendis.

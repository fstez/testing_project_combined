# Task 7 – Integratsioonitestid

**Kestus:** ~15 min

## Info (20%)
Integratsioonitest kinnitab, et backend, välised API-d ja logimine toimivad koos. HTTP tasandi kontroll (nt `requests` + `responses`) imiteerib tootmiskäitumist ilma väliseid teenuseid ülekoormamata.

## Ülesanne (60%)
- Kirjuta `tests-integration/test_koostoime.py` testid, mis kasutavad FastAPI `TestClient`-i ja mokivad välise API `responses` teegiga.
- Lisa test edukale ja tõrksel (HTTP 502) stsenaariumile ning kontrolli, et logis on vastav sissekanne.
- macOS/Linux: `source .venv/bin/activate && pytest tests-integration -v`; Windows PowerShell: `.\.venv\Scripts\Activate.ps1; pytest tests-integration -v`. Salvesta logi `docs/results/integration/integration.log` ja lisa pass/fail tingimus testiplaanis.

## Valmisoleku kontroll (20%)
- CI-s saab jooksutada `pytest tests-integration -v` ilma päris API-sid tabamata.
- Logifail ja pass/fail tingimus on kirjas `docs/results/integration/` ja `docs/testplan.md`.

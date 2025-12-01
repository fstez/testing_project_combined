# Task 8 – GitHub Actions CI

**Kestus:** ~15 min

## Info (20%)
GitHub Actions võimaldab defineerida testijooksud YAML-failis. Selge töövoog annab automaatse tagasiside iga push'i või pull request'i puhul.

## Ülesanne (60%)
- Loo fail `.github/workflows/tests.yml`, mis käivitub `push` ja `pull_request` sündmustel harule `main`.
- Lisa job `python-tests` (setup-python → `pip install -r backend/requirements.txt` → `pytest tests-python tests-integration`) ja job `js-tests` (setup-node → `npm ci` → `npm test`).
- Kasuta `actions/upload-artifact` sammu `docs/results/pytest/**` ja `docs/results/jest/**` salvestamiseks ning dokumenteeri töövoo link `docs/results/ci/README.md` failis.

## Valmisoleku kontroll (20%)
- Workflow peatub, kui mõni test kukub.
- CI jooksu link ja artefaktid on kirjeldatud `docs/results/ci/`.

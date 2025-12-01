# Task 4 – Pytest ühikutestid

**Kestus:** ~15 min

## Info (20%)
Pytest toetab lühikesi, loetavaid teste ning fixture'ite abil saab FastAPI klienti ja mokitud HTTP päringuid korduskasutada.

## Ülesanne (60%)
- Loo vähemalt viis testi `tests-python/` kaustas (edukas vastus, välise vea käsitlus, ajatempli kontroll, skeem, logi).
- Kasuta `TestClient` fixture'it ja `monkeypatch`/`responses` abil mokka väliskõned deterministlikuks.
- macOS/Linux: `source .venv/bin/activate && pytest tests-python -v`; Windows PowerShell: `.\.venv\Scripts\Activate.ps1; pytest tests-python -v`. Salvesta logi `docs/results/pytest/pytest.log` ja viita testiplaanis.

## Valmisoleku kontroll (20%)
- `pytest tests-python -v` lõpeb roheliselt ja logi on `docs/results/pytest/`.
- Testide nimed kirjeldavad käitumist ning viide lisatud `docs/testplan.md`.

# Task 2 – Projekti seadistus ja avalikud API-d

**Kestus:** ~15 min

## Info (20%)
JSONPlaceholder ja Rick & Morty API on avalikud REST teenused. Sinu FastAPI backend peab need koondama ühte etteaimatavasse skeemi, mida hiljem testid ja koormusstsenaariumid kasutavad.

## Ülesanne (60%)
- macOS/Linux: `cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`; Windows PowerShell: `cd backend; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt`.
- Käivita `uvicorn backend.main:rakendus --reload` ja testi `GET /status`.
- Täienda `/api/koond`, et mõlemad API-d kutsutakse ja vastus sisaldab `postitus`, `tegelane`, `allikad`, `paastikuAeg`.
- Lisa logid ning HTTP 502 detailid vigade korral.

## Valmisoleku kontroll (20%)
- `uvicorn` jookseb ja `curl http://localhost:8000/api/koond` tagastab skeemi.
- Veaolukorras naaseb 502 koos detailse kirjega; juhend lisatud `backend/README.md`.

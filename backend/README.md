# Backend – FastAPI koondteenus

## Eeldused
- Python 3.11+
- Virtuaalkeskkond (soovituslik)

## Kiirstart
**macOS/Linux**
```bash
cd /Users/robinrattasep/testing_project/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd /Users/robinrattasep/testing_project
uvicorn backend.main:rakendus --reload
# või backend kaustast:
# uvicorn main:rakendus --reload --app-dir /Users/robinrattasep/testing_project/backend
```

**Windows (PowerShell)**
```powershell
cd C:\Users\<user>\testing_project\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd C:\Users\<user>\testing_project
uvicorn backend.main:rakendus --reload
# või backend kaustast:
# uvicorn main:rakendus --reload --app-dir C:\Users\<user>\testing_project\backend
```

Endpointid:
- `GET /status` – tervisekontroll.

![status]({95C80979-ABBB-474A-8052-842093AB6A9B}.png)
![status2]({62089589-382C-4B5B-9208-6487EC2791C1}.png)


- `GET /api/koond` – kombineeritud JSONPlaceholder + Rick & Morty vastus.

![api_koond]({6BF84280-168C-415C-9A6C-C114BDB5F4DB}.png)
![api_koond2]({3E54FD94-0CC1-4AC5-9D58-7F01C00DE0ED}.png)

-  Veaolukorras naaseb 502 koos detailse kirjega;

![viga](image.png)
![viga2]({93D5486C-E9F5-4ABF-8FCD-1CDD259D80F9}.png)

## Kvaliteedivihjed
- Muuda URL-e keskkonnamuutujatega, kui testid nõuavad.
- Logi kõik vead näitamaks riskide maandamist.

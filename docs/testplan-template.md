# Testiplaani mall

---

# Testiplaan – Task 2: Projekti seadistus ja avalikud API-d

**Projekti nimi:** API kvaliteedikontroll   
**Autorid ja kuupäev:** Daria, 26.11.2025  

## 1. Sissejuhatus
**Eesmärk** – testida FastAPI backendit, mis ühendab JSONPlaceholderi ja Rick & Morty avalike API-de andmed üheks ennustatavaks skeemiks.  
**Testimise kontekst:** veenduda, et `/api/koond` tagastab korrektse JSONi ja töötleb korrektselt väliste API-de vigu (HTTP 502).

## 2. Ulatus
**Kaasatud komponendid:**
- Backend FastAPI (`backend/main.py`)
- Avalikud API-d: JSONPlaceholder ja Rick & Morty
- Endpoints: `/status` ja `/api/koond`
- Logimine ja error handling

## 3. Nõuded ja aktsepteerimiskriteeriumid
| Nõue | Testimeetod | Oodatav tulemus |
|-------|-------------|----------------|
| `/status` tagastab `200 OK` | GET /status | {"olek": "aktiivne", "allikas": "Kvaliteedijälg API"} |
| `/api/koond` koondab mõlema API andmed | GET /api/koond | JSON sisaldab `postitus`, `tegelane`, `allikad`, `paastikuAeg` |
| Logimine | vaata serveri logisid | INFO logid väliste API päringute ja koondamise kohta |
| Viga välises API-s | muuda URL katkise või eksisteerimata | HTTP 502 koos `detail`: sonum, siht, pohjus |

## 4. Riskid ja maandus
| Risk | Mõju | Tõenäosus | Maandus |
|------|------|------------|---------|
| Välise API kättesaamatus | Kõik koondatud andmed puuduvad | Keskmine | Tagada error handling 502 |
| Vale JSON skeem | Testid läbivad ebaõigesti | Madal | Kontrollida kõiki väljastatud välju |

## 5. Meetodid ja tööriistad
- Ühikutestid: FastAPI endpoints
- Integratsioonitestid: `/api/koond` väliste API-dega
- Automaatika: Python `pytest`, HTTP päringud käsitsi `curl` või `http`

## 6. Testkeskkonnad ja andmed
- Python: 3.13
- Testandmed: avalikud API-d (`JSONPlaceholder`, `Rick & Morty`)
- Mock-serverid võivad kasutada vigade simuleerimiseks katkiseid URL-e

## 7. Ajajoon ja vastutajad
| Tegevus | Vastutaja | Aeg |
|----------|-----------|-----|
| Venv loomine ja sõltuvuste paigaldus | Daria | 5 min |
| Serveri käivitamine ja `/status` testimine | Daria | 2 min |
| `/api/koond` korrektse skeemi test | Daria | 2 min |
| Vigade käsitlemise test | Daria | 10 min |

## 8. Raporteerimine
- Testitulemused salvestatakse: `docs/results/task2.md` ja `backend/README.md`
- Edukriteerium: kõik kriitilised testid (`/api/koond` ja 502 error handling) läbivad

--- 

# Testiplaan – Task 3: GA4 

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – A/B katse  
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** Kontrollige, et A/B-testi sündmused (`variant_vaade` ja `variant_vahetus`) saadetakse korrektselt Google Analyticsisse.

## 2. Ulatus
**Kaasatud moodulid:**  
- Frontend (`index.html`, `app.js`, `ab.js`)  
- Backend (`GET /api/koond`)  
- GA4 teenus ja DebugView  

## 3. Nõuded ja aktsepteerimiskriteeriumid

**Funktsionaalsed nõuded:**  
1. GA4 skript on lisatud faili `index.html` ja kasutab identifikaatorit `G-XXXXTEST`.    
2. Sündmused `variant_vaade` ja `variant_vahetus` kutsutakse välja iga kord, kui kuvatakse paigutus ja vahetatakse varianti.   
3. Network-paneelis on näha päringud GA4 serverile (`collect`).   

| Kontrollpunkt | Kriteerium | 
|----------------|------------|
| GA4 skript on olemas | `index.html` sisaldab `<script src="https://www.googletagmanager.com/gtag/js?...">` |
| `variant_vaade` sündmus | Event saadetakse Network → collect, sisaldab `variant`, `sessioonId`, `katsestaadium` |
| `variant_vahetus` sündmus | Event saadetakse pärast nuppu "Vaheta varianti" vajutamist |
| Ekraanipildid | Võrgupäringute ja console.log’i kuvatud sündmused on salvestatud `docs/results/analytics/` |

## 4. Riskid ja maandus
| Kirjeldus | Mõju | Tõenäosus | Maandus |
|-----------|-------|------------|---------|
| GA4 päringud ei lähe läbi | Testi ebaõnnestumine | Keskmine | Kasutada debug_mode ja mock GA4 tunnust |
| Backend `/api/koond` ei tööta | Variantide info ei laaditu | Kõrge | Kontrolli backendi käivitust enne testi |
| Brauseri CORS / cookie hoiatused | Mõned sündmused ei lähe läbi | Keskmine | Testida localhost, vajadusel lubada CORS |

## 5. Meetodid ja tööriistad
- **Testimise liigid:** A/B testide sündmuste kontroll, integratsioon frontend+backend, võrgu päringud  
- **Automaatika vahendid:** DevTools, console.log, Python HTTP server (`python -m http.server`), GitHub Actions (CI)  

## 6. Testkeskkonnad ja andmed
**Konfiguratsioonid:**  
- Python: 3.10+ (HTTP server)  
- Node.js / npm: vajadusel frontend build  
- Browser: Chrome / Firefox (DevTools Network)  

**Testandmete allikad:**  
- Mock GA4 tunnus: `G-XXXXTEST`  
- API sandbox: `GET /api/koond`  

## 7. Ajajoon ja vastutajad
| Tegevus | Vastutaja | Aeg |
|----------|---------------|-------|
| Sündmuste testimine (`variant_vaade`, `variant_vahetus`) | Daria | 10 min |
| Network-paneeli ja DebugView kontrollimine | Daria | 5 min |
| Ekraanipiltide kogumine ja aruande koostamine | Daria | 5 min |

## 8. Raporteerimine
- **Aruannete formaadid:** `docs/results/analytics/`
- **Edukriteeriumid:**  
  - Kõik sündmused (`variant_vaade` ja `variant_vahetus`) ilmuvad Network → collect  
  - Ekraanipildid on salvestatud kausta `docs/results/analytics/`  
  - Console.log näitab õiged event objektid  

---

# Testiplaan – Task 4: Pytest 

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – FastAPI koondteenuse backend  
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** tagada FastAPI-tagapõhja stabiilne testimine Pytesti abil

## 2. Ulatus
**Kaasatud moodulid:**  
- Backend (`backend/main.py`)  
  - `/status`  
  - `/api/koond`  
  - `hanki_andmed()`  
- Testid kaustas `tests-python/`  
- Logi fail `docs/results/pytest/pytest.log`

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded
1. `/status` tagastab oleku `"aktiivne"` ja metainfo.  
2. `/api/koond` ühendab kaks välisallikat ja tagastab õige skeemiga JSON.  
3. Välise API tõrge põhjustab vastuse koodiga **502**.  
4. Logid salvestatakse Pytesti jooksutamisel.

| Kontrollpunkt | Kriteerium |
|----------------|------------|
| TestClient töötab | `client.get()` tagastab 200 / 502 |
| Vea käsitlus | `hanki_andmed()` viskab vea ja `/api/koond` → 502 |
| Skeemi kontroll | `postitus.pealkiri`, `tegelane.nimi`, `allikad` olemas |
| Logi olemasolu | `docs/results/pytest/pytest.log` on loodud |

## 4. Riskid ja maandus
| Kirjeldus | Mõju | Tõenäosus | Maandus |
|-----------|-------|------------|---------|
| Välis-API ei vasta | Test kukub läbi | Kõrge | Kasutada monkeypatch mokitamiseks |
| Vale skeem backendis | Väline API muutub | Keskmine | Skeemi testid püüavad vea kinni |
| Pytest ei leia mooduleid | Arenduskeskkonna viga | Keskmine | Kontrollida `PYTHONPATH` ja imports |
| Logi ei salvestu | Testplaani rikkumine | Madal | Suunata pytesti väljund logifaili |

## 5. Meetodid ja tööriistad

- Pytest — unit и integration testid
- FastAPI TestClient — endpointide testimine
- monkeypatch — väliste API-de imitatsioon
- responses (valikuline) — HTTP-vastuste salvestamine

## 6. Testkeskkonnad ja andmed

- Python: 3.10+ (HTTP server) 
- Käivitamise käsk: `pytest tests-python -v` 
- salvestamine pytest.log-faili `pytest tests-python -v --capture=no > docs/results/pytest/pytest.log 2>&1` 

## 7. Ajajoon ja vastutajad
| Tegevus | Vastutaja | Aeg |
|----------|---------------|-------|
| Testide kirjutamine | Daria | 10 -15 min |
| Pytest käivitamine + logi salvestamine | Daria | 5 min |

## 8. Raporteerimine

- Tulemused salvestatakse: `docs/results/pytest/pytest.log`
- kõik testid on rohelised
- logi on loodud

---

# Testiplaan – Task 5: JavaScript testid

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – FastAPI frontend A/B testid  
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** tagada frontend/ab.js funktsioonide korrektne testimine Jest abil Node.js keskkonnas

## 2. Ulatus

**Kaasatud moodulid:**  
- Frontend (`frontend/ab.js`)  
  - valiVariant()  
  - vahetaVariant()  
  - looLayoutHTML()  
  - looSyndmuseKeha()  
  - localStorage salvestusloogika  
- Testid kaustas `tests-js/`  
- Logi fail `docs/results/jest/jest.log`

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded
1. `valiVariant` tagastab olemasoleva variandi
2. `vahetaVariant` muudab varianti korrektselt.  
3. `looSyndmuseKeha` lisab sündmuse metaandmed.  
4. Andmete salvestamine `localStorage`-sse toimub mock-objekti ja fallbacki kaudu.  
5. Logid salvestatakse testide käivitamisel.

| Kontrollpunkt | Kriteerium |
|----------------|------------|
| Funktsioonide testimine | valiVariant, vahetaVariant, looLayoutHTML, looSyndmuseKeha töötavad ootuspäraselt |
| localStorage mock | andmete salvestamine ja tagasivõtmine töötab fallback-mockiga |
| Skeemi kontroll | looSyndmuseKeha sisaldab variant, katsestaadium, sessioonId |
| Logi olemasolu | docs/results/jest/jest.log on loodud |

## 4. Riskid ja maandus

| Kirjeldus | Mõju | Tõenäosus | Maandus |
|-----------|-------|------------|---------|
| Funktsioonid muutuvad | Testid kukuvad läbi | Keskmine | Testide hooldus ja uuendamine |
| localStorage ei tööta | Andmete salvestus ebaõnnestub | Madal | Mock ja fallback-loogika |
| Jest ei käivitu | Node.js keskkonna probleem | Keskmine | Kontrollida Node ja npm versiooni |
| Logi ei salvestu | Testplaani rikkumine | Madal | Suunata Jest väljund logifaili |

## 5. Meetodid ja tööriistad
 
- Jest — ühik- ja integratsioonitestid Node.js-is
- Mockimine— `global.localStorage` lihtsa objektina
- npm test — testide käivitamine
- Logi salvestamine — väljundi suunamine `docs/results/jest/jest.log`

## 6. Testkeskkonnad ja andmed

- Node.js 18+  
- npm 9+  
- Käivitamise käsk: `cd tests-js`, `npm install`, `npm test`
- salvestamine jest.log-faili `npm test > ..\docs\results\jest\jest.log 2>&1` 

## 7. Ajajoon ja vastutajad
| Tegevus | Vastutaja | Aeg |
|----------|---------------|-------|
| Testide kirjutamine | Daria | 10 -15 min |
| Npm testi käivitamine + logi salvestamine | Daria | 5 min |

## 8. Raporteerimine

- Tulemused salvestatakse: `docs/results/jest/jest.log`
- kõik testid on rohelised
- logi on loodud

---

# Testiplaan – Task 6: A/B testimine

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – A/B testimine frontendis 
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** tagada A/B testi valikuvõimaluse, salvestamise ja sündmuste logimise korrektne toimimine.

## 2. Ulatus

**Kaasatud moodulid:**  
- Frontend (`frontend/ab.js`)  
  - valiVariant()  
  - vahetaVariant()  
  - looLayoutHTML()  
  - looSyndmuseKeha()  
  - localStorage salvestusloogika  
- Frontend (`frontend/app.js`)  
  - nupp variandi vahetamiseks  
  - sündmuste vallandamine `variant_vaade` ja `variant_vahetus`  
- Logid salvestatud kaustas `docs/results/analytics/`

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded
1. Mõlemad variandid on selgelt eristatavad (unikaalne klass/atribuut).  
2. `valiVariant` ja `vahetaVariant` tagastavad deterministliku tulemuse.  
3. `looLayoutHTML` kuvab õige HTML vastavalt variandile.  
4. `localStorage` salvestab ja taastab kasutaja valiku.  
5. Sündmused `variant_vaade` ja `variant_vahetus` vallanduvad õigel ajal.  
6. Logid salvestatakse automaatselt või käsitsi failidesse `docs/results/analytics/`.

| Kontrollpunkt | Kriteerium |
|----------------|------------|
| Variandi eristamine | Mõlemal variandil on unikaalne klass või ID |
| Funktsioonide töö | valiVariant, vahetaVariant, looLayoutHTML töötavad  |
| localStorage | Valik salvestub ja taastub õigesti |
| Sündmuste vallandamine | GA sündmused `variant_vaade` ja `variant_vahetus` registreeritud |
| Logi olemasolu | docs/results/analytics/ kaustas logifailid olemas |

## 4. Riskid ja maandus

| Kirjeldus | Mõju | Tõenäosus | Maandus |
|-----------|-------|------------|---------|
| Variandi eristamine ebaõnnestub | GA ei registreeri õigeid sündmusi | Keskmine | Kontrollida HTML klassid ja ID-d |
| localStorage ei tööta | Valik ei säili | Madal | Kontrollida fallback-loogikat ja mockimist |
| Sündmused ei vallandu | Analüüs ei tööta | Keskmine | Lisada testid ja logimine sündmuste jaoks |
| Logi ei salvestu | Testplaani rikkumine | Madal | Automaatne salvestamine või käsitsi eksport |

## 5. Meetodid ja tööriistad

- GA4 debug-mode jälgimine sündmuste registreerimiseks  
- localStorage mockimine testide käigus  

## 6. Testkeskkonnad ja andmed

- Brauser: Chrome / Firefox  
- Käivitamise käsk: avada `frontend/index.html` brauseris  
- Logide salvestamine: `docs/results/analytics/`

## 7. Ajajoon ja vastutajad

| Tegevus | Vastutaja | Aeg |
|----------|---------------|-------|
| Variandi loogika ja HTML testimine | Daria | 5-10 min |
| Nupu ja sündmuste kontroll brauseris | Daria | 5 min |
| Logide salvestamine | Daria | 5 min |

## 8. Raporteerimine

- Kontrollitakse, et mõlemad variandid ilmuvad GA sündmustes  

---

# Testiplaan – Task 7: Integratsioonitestid

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – FastAPI backend integratsioonitestid 
**Autorid ja kuupäev:** Daria, 26.11.2025 

**Eesmärk:** tagada, et backend, välised API-d ja logimine töötavad koos ning integratsioonitestid toimivad ilma päris teenuseid tabamata.

## 2. Ulatus

**Kaasatud moodulid:**  
- Backend (`backend/main.py`)  
  - `/api/koond` endpoint  
- Testid kaustas tests-integration/
- Logi fail: `docs/results/integration/integration.log`

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded

1. Endpoint /api/koond tagastab eduka vastuse välisteenuste korrektsel töötamisel.
2. Endpoint tagastab HTTP 502 ja õige detaili objekti, kui mõni väline teenus ei tööta.
3. Loogikates fikseeritakse sündmusi nii edukate kui ka ebaõnnestunud päringute jaoks.

| Kontrollpunkt         | Kriteerium                                                |
| --------------------- | --------------------------------------------------------- |
| Edukas API | `/api/koond` tagastab 200 ja õige keha |
| Välise API viga | `/api/koond` tagastab 502 ja detail-sõnumi |
| Logimine | Kõik sissekanded salvestatakse `integration.log` |

## 4. Riskid ja maandus

| Kirjeldus                    | Mõju                 | Tõenäosus | Maandus                                     |
| ---------------------------- | -------------------- | --------- | ------------------------------------------- |
| Välised teenused ei reageeri | Testid ebaõnnestuvad | Madal     | Kasutada `responses` mokke                  |
| Logi faili ei kirjutata      | Testplaani rikkumine | Madal     | Kontrollida faili teed ja UTF-8 kodeeringut |
| Endpoint muutub              | Testid ebaõnnestuvad | Keskmine  | Testide hooldus ja uuendamine               |

## 5. Meetodid ja tööriistad

- FastAPI TestClient integratsioonitestide jaoks
- `pytest` testide käivitamiseks
- `responses` väliste API-de mockimiseks
- Logide salvestamine failile: `docs/results/integration/integration.log`

## 6. Testkeskkonnad ja andmed

- Python 3.12+
- `.\.venv\Scripts\Activate.ps1` 
- `pytest tests-integration -v`
- Logide salvestamine: `docs/results/integration/integration.log`

## 7. Ajajoon ja vastutajad

| Tegevus                                    | Vastutaja | Aeg       |
| ------------------------------------------ | --------- | --------- |
| Testide kirjutamine                        | Daria     | 10–15 min |
| Testide käivitamine ja logide salvestamine | Daria     | 5 min     |

## 8. Raporteerimine

- Tulemused salvestatakse: `docs/results/integration/integration.log`
- Kõik testid peavad olema rohelised (PASS)
- Logis on kirjed edukatest ja ebaõnnestunud API päringutest

---

# Testiplaan – Task 8: GitHub Actions CI

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – CI automatiseeritud testitöövoog  
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** tagada, et Python- ja JavaScript-testid käivitatakse automaatselt iga push'i ja pull request’i puhul ning testilogid ja CI töövoo info arhiveeritakse projekti dokumentatsiooni alla.

## 2. Ulatus

**Kaasatud komponendid:**
- GitHub Actions workflow `.github/workflows/tests.yml`
- Python testid:  
  - `tests-python/`  
  - `tests-integration/`
- JavaScript testid:  
  - `tests-js/`
- Artefaktide salvestamine:  
  - `docs/results/pytest/**`  
  - `docs/results/jest/**`
- CI dokumentatsioon:  
  - `docs/results/ci/README.md`

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded

| Kontrollpunkt | Kriteerium |
|--------------|------------|
| Workflow käivitus | CI käivitub `push` ja `pull_request` sündmustel harule `main` |
| Python testid | Keskkond seadistatakse (Python 3.11), paigaldatakse sõltuvused, käivitatakse `pytest tests-python tests-integration` |
| JS testid | Node 20 keskkond, `npm ci`, `npm test` |
| Artefaktide salvestamine | Logid arhiveeritakse: `pytest-logid` ja `jest-logid` |
| CI dokumentatsioon | Fail `docs/results/ci/README.md` sisaldab töövoo linki ja artefaktide nimekirja |

## 4. Riskid ja maandus

| Kirjeldus | Mõju | Tõenäosus | Maandus |
|----------|-------|-----------|---------|
| Sõltuvuste paigaldamine ebaõnnestub | CI katkeb | Keskmine | Kontrollida `requirements.txt` ja `package.json` |
| Testid kukuvad ja peatavad workflow | Arendusvoog katkeb | Keskmine | Parandada testid või koodi |
| Artefaktide tee vale | Logisid ei arhiveerita | Madal | Kontrollida kataloogide olemasolu |
| CI README ei genereeru | Dokumentatsioon puudulik | Madal | Kontrollida YAML-s ridade joondust |

## 5. Meetodid ja tööriistad

- **GitHub Actions** CI töövoogude loomiseks  
- **actions/checkout** – repo kloonimine  
- **actions/setup-python** – Python keskkond  
- **actions/setup-node** – Node keskkond  
- **pytest** – Python testimise tööriist  
- **npm test** – JS testide käivitamine  
- **actions/upload-artifact** – logide arhiveerimine  
- Bash käsud README genereerimiseks

## 6. Testkeskkond ja eeldused

- GitHub repository  
- Workflow fail `.github/workflows/tests.yml`  
- Testide käsitsi käivitamise kontroll:
  - `pytest tests-python tests-integration`
  - `cd tests-js && npm test`


## 7. Ajajoon ja vastutajad

| Tegevus | Vastutaja | Aeg |
|---------|-----------|------|
| Workflow loomine | Daria | 5–10 min |
| Testide integreerimine workflow’sse | Daria | 5–10 min |
| Artefaktide ja README genereerimine | Daria | 5 min |

## 8. Raporteerimine

- CI logid salvestatakse GitHub Actions → Artifacts:
  - `pytest-logid`
  - `jest-logid`
  - `ci-readme`
- Projekti repo dokumentatsioon sisaldab:
  - `docs/results/ci/README.md` – viide viimasele CI jooksule ja logide artefaktidele
- Eduka testijooksu puhul mõlemad job'id on rohelised (PASS)

---

# Testiplaan – Task 9: Locust koormustest

## 1. Sissejuhatus

**Projekti nimi:** Kvaliteedijälg – backend koormustestimine  
**Autorid ja kuupäev:** Daria, 26.11.2025  

**Eesmärk:** Kontrollida, kuidas backend talub 20–50 samaaegset kasutajat ja kas API latentsus jääb lubatud piiridesse. Genereerida CSV ja HTML aruanded dokumentatsiooni jaoks.

## 2. Ulatus

**Kaasatud komponendid:**
- Backend (`backend/`)
- Koormustest skriptid (`tests-performance-locust/locustfile.py`)
- Aruanded:
  - CSV: `docs/results/locust/koormus_*.csv`
  - HTML: `docs/results/locust/koormus.html`
  - Ekraanipildid: `docs/results/locust/koormus.md`

## 3. Nõuded ja aktsepteerimiskriteeriumid

| Kontrollpunkt | Kriteerium |
|---------------|------------|
| Backend töötab | `uvicorn backend.main:rakendus --reload` |
| Locust test | 50 kasutajat, 5 kasutajat/sek, kestus 5 min |
| Aruannete genereerimine | CSV ja HTML `docs/results/locust/` kaustas |

**Edukriteeriumid:**
- Test läbitakse ilma kriitiliste vigadeta  
- CSV ja HTML aruanded on õigesti genereeritud  
- Ekraanipildid on lisatud 

## 4. Riskid ja maandus

| Risk | Mõju | Tõenäosus | Maandus |
|------|------|-----------|---------|
| Backend ei tööta | Test ebaõnnestub | Keskmine | Kontrollida `uvicorn` käivitamist |
| Locust pole paigaldatud | Test ebaõnnestub | Madal | `pip install locust` `.venv` keskkonnas |
| Aruande failid ei genereeru | Dokumentatsioon puudulik | Madal | Kontrollida `--csv` ja `--html` teid |

## 5. Meetodid ja tööriistad

- **Locust** – koormustestimine  
- **Uvicorn** – backend server  
- **Excel / LibreOffice / Google Sheets** – CSV vaatamiseks  
- **Brauser** – HTML aruande vaatamiseks ja ekraanipiltide tegemiseks  

## 6. Testkeskkond ja eeldused

- Windows või macOS/Linux  
- Python virtuaalne keskkond `.venv`  
- Paigaldatud backend sõltuvused  
- Testskriptid `tests-performance-locust/`  
- Aruandekataloog: `docs/results/locust/`

## 7. Ajajoon ja vastutajad

| Tegevus | Vastutaja | Aeg |
|---------|-----------|-----|
| Backend kontroll | Daria | 2 min |
| Locust koormustesti käivitamine | Daria | 8 min |
| Ekraanipiltide tegemine ja lisamine | Daria | 5 min |

## 8. Raporteerimine

- CSV aruanded: `koormus_stats.csv`, `koormus_failures.csv` jne  
- HTML aruanne: `koormus.html`  
- Ekraanipildid salvestatakse `docs/results/locust/`
- Testi edukus: 
  - Backend on vastu pidanud kõigile kasutajatele;
  - Aruanded on genereeritud; 
  - Screenshotid on lisatud;
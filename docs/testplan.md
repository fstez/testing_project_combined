# Testiplaan – Kvaliteedijälg

- **Projekti nimi:** Kvaliteedijälg  
- **Autorid ja kuupäev:** Tudeng – 24.11.2025  
- **Versioon:** 1.0

---

## 1. Sissejuhatus

Projekti *Kvaliteedijälg* eesmärk on luua mitmeastmeline testimiskeskkond, mis ühendab FastAPI backend’i, HTML/JavaScript frontend’i, GA4 analüütika, A/B testimise, CI töövoo ja Locusti koormustestimise.  
Testiplaan määratleb kvaliteedihindamise eesmärgid, ulatuse, riskid, vastu­võtukriteeriumid ja kasutatavad tööriistad.

Projekti kontekst:
- Õppeprojekt reaalsete vahenditega  
- Kaasatud avalikud API-d (JSONPlaceholder & Rick and Morty API)  
- Automaatika (Pytest, Jest, CI torustik)  
- Jõudlustestid (Locust)  
- A/B katse küljenduste võrdlemiseks

---

## 2. Ulatus

### Kaasatud komponendid:
- **Backend (FastAPI)**
  - `/api/koond` endpoint  
  - Väliste API-de (JSONPlaceholder, Rick & Morty) päring  
  - Andmete normaliseerimine ühtsesse skeemi  
- **Frontend (HTML/JS)**
  - Andmete laadimine backendist  
  - A/B variantide haldus via localStorage  
  - GA4 sündmuste logimine  
- **GA4**
  - Sündmused: `variant_vaade`, `variant_vahetus`  
- **CI/CD**
  - GitHub Actions testitorustik (Pytest + Jest)  
- **Koormustestid**
  - Locust, 20–50 kasutajat, 3-minutilised jooksud  
- **Integratsioonitestid**
  - Mockitud välised API-d (responses + TestClient)

### Välistatud:
- Autentimine, sessioonid  
- Andmebaasid  
- Täielik turvatestimine  
- Visuaalne UI-regressioon  
- Mobile layout spetsiaalne testimine  

---

## 3. Nõuded ja aktsepteerimiskriteeriumid

### Funktsionaalsed nõuded:

| ID | Nõue | Aktsepteerimiskriteerium |
|----|------|---------------------------|
| F-01 | `/api/koond` tagastab koondandmed | Vastus sisaldab `count` ja `items` välju |
| F-02 | API pärib 2 avalikku teenust | Mõlemad API-d vastavad või fallback → 500 |
| F-03 | Andmed normaliseeritakse skeemi | Igal elemendil on `source/id/title/extra/timestamp` |
| F-04 | Frontend laeb ja kuvab andmeid | Brauser näitab kuni 10 kirjet |
| F-05 | A/B varianti saab vahetada | Toggle muudab localStorage väärtust |
| F-06 | GA4 saadab sündmused | GA4 DebugView näitab mõlemat sündmust |

### Mittenõuded:

| ID | Mittenõue | Kriteerium |
|----|-----------|-----------|
| NF-01 | Jõudlus | API vastab < 500ms kuni 50 kasutaja puhul |
| NF-02 | Stabiilsus | CI peab läbima kõik testid |
| NF-03 | Turvalisus | Põhiturvalisus tagatud (ei hinnata süvitsi) |

---

## 4. Riskid ja maandus

| ID | Risk | Mõju | Tõenäosus | Maandus |
|----|------|-------|-----------|----------|
| R-01 | Avalik API ei tööta | Keskmine | Keskmine | Mockidega testimine |
| R-02 | GA4 ei kogu sündmusi | Madal | Keskmine | DebugView kontroll |
| R-03 | CI sõltub npm/pip pakettidest | Kõrge | Keskmine | Versioonide lukustamine |
| R-04 | Koormustestid tekitavad throttlingut | Madal | Madal | Kasutajate arvu piiramine |
| R-05 | A/B toggle ei salvestu | Keskmine | Madal | Jest testid localStorage’ile |

---

## 5. Meetodid ja tööriistad

### Testimise liigid:
- **Ühikutestid (Pytest)**  
  - Skeemikontroll, timestamp, error handling  
- **Integratsioonitestid**  
  - FastAPI TestClient, responses mock  
- **Frontend testid (Jest)**  
  - A/B loogika, sündmuste mudelid, localStorage  
- **A/B testimine**  
  - Variandi salvestus & sündmused  
- **Koormustestid (Locust)**  
  - `/api/koond` 20–50 kasutajaga  
- **Analüütika test**  
  - GA4 DebugView ja sündmuste võrguinspekteerimine  

### Tööriistad:
- Python 3.10, Node 18  
- FastAPI, Uvicorn  
- Pytest, Jest  
- Locust  
- GitHub Actions  
- GA4 (gtag.js)  

---

## 6. Testkeskkonnad ja andmed

### Keskkonnad:
| Komponent | Versioon |
|----------|----------|
| Python | 3.10 |
| Node | 18.x |
| FastAPI | 0.110+ |
| Jest | 29+ |
| Locust | 2.23+ |
| OS | Ubuntu / macOS |

### Testandmed:
- Avalike API-de sandbox andmed  
- Mockitud vastused integratsioonitestide jaoks  
- A/B variandi localStorage väärtused (`A`, `B`)  

---

## 7. Ajajoon ja vastutajad (10h projekt)

| Aeg | Tegevus | Vastutaja |
|-----|-----------|------------|
| 0.5h | Nõuete analüüs | Tudeng |
| 1h | Backend API | Tudeng |
| 1h | Frontend A/B + API ühendus | Tudeng |
| 1h | GA4 integreerimine | Tudeng |
| 1h | Pytest ühikutestid | Tudeng |
| 1h | Jest testid | Tudeng |
| 1h | Integratsioonitestid | Tudeng |
| 1h | CI seadistus | Tudeng |
| 1h | Locust koormustestid | Tudeng |
| 1h | Dokumenteerimine | Tudeng |

---

## 8. Raporteerimine

Aruanded salvestatakse kataloogi `docs/results/`:

| Testiliik | Asukoht |
|-----------|----------|
| Pytest | `docs/results/pytest/` |
| Jest | `docs/results/jest/` |
| Integratsioonitestid | `docs/results/integration/` |
| Locust | `docs/results/locust/` |
| GA4 | `docs/results/analytics/` |
| CI logid | `docs/results/ci/` |

### Edukriteeriumid:
- Kõik kriitilised testid rohelised  
- CI torustik läbiv  
- GA4 sündmused nähtavad DebugView’s  
- Koormustestid < 500ms keskmise vastusega  

---

**Dokument valmis.**  
Selle saab kohe committida ja esitada.

---

Kui soovid — сделаю Task 2 сразу.

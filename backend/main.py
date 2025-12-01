"""FastAPI rakendus avalike API-de koondamiseks ja testimiseks."""
from datetime import datetime, timezone
import logging
from typing import Any, Dict

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

RAKENDUSE_NIMI = "Kvaliteedijälg API"
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts/1"
RICK_MORTY_URL = "https://rickandmortyapi.com/api/character/1"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kvaliteedijalg.backend")

rakendus = FastAPI(title=RAKENDUSE_NIMI, version="0.1.0")

rakendus.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def hanki_andmed(url: str) -> Dict[str, Any]:
    """Pärib välise API ja tagastab JSON andmed tõrke korral HTTP veana."""
    try:
        logger.info("Pärin välise API", extra={"siht": url})
        vastus = requests.get(url, timeout=5)
        vastus.raise_for_status()
        return vastus.json()
    except requests.RequestException as viga:
        logger.error("Välise API tõrge", exc_info=viga, extra={"siht": url})
        raise HTTPException(
            status_code=502,
            detail={
                "sonum": "Välise teenuse tõrge",
                "siht": url,
                "pohjus": str(viga),
            },
        ) from viga


@rakendus.get("/status")
def tervise_kontroll() -> Dict[str, str]:
    """Lihtne töökindluse kontroll, mida saab monitoringus pingida."""
    return {"olek": "aktiivne", "allikas": RAKENDUSE_NIMI}


@rakendus.get("/api/koond")
def koonda_andmed() -> Dict[str, Any]:
    """Kombineerib JSONPlaceholderi ja Rick & Morty andmed testitavasse struktuuri."""
    allikad = [JSONPLACEHOLDER_URL, RICK_MORTY_URL]
    try:
        postitus = hanki_andmed(JSONPLACEHOLDER_URL)
        tegelane = hanki_andmed(RICK_MORTY_URL)

        koond = {
            "postitus": {
                "id": postitus.get("id"),
                "pealkiri": postitus.get("title"),
                "katkend": postitus.get("body", "")[:80],
            },
            "tegelane": {
                "id": tegelane.get("id"),
                "nimi": tegelane.get("name"),
                "staatuse": tegelane.get("status"),
            },
            "allikad": allikad,
            "paastikuAeg": datetime.now(timezone.utc).isoformat(),
        }
        logger.info("Koondan API vastuseid", extra={"allikad": allikad})
        return koond
    except HTTPException as viga:
        logger.error("Koondamise käigus ilmnes viga", exc_info=viga, extra={"allikad": allikad})
        raise viga
    except Exception as viga:
        logger.critical("Ettearvamatu viga koondamisel", exc_info=viga, extra={"allikad": allikad})
        raise HTTPException(
            status_code=502,
            detail={
                "sonum": "Sisene serveri viga koondamisel",
                "allikad": allikad,
                "pohjus": str(viga),
            },
        ) from viga

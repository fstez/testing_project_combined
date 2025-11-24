"""FastAPI rakendus avalike API-de koondamiseks ja testimiseks."""
from datetime import datetime, timezone
import logging
from typing import Any, Dict

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

RAKENDUSE_NIMI = "Kvaliteedijälg API"

# Avalike API-de põhiressursid
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts/1"
RICK_MORTY_URL = "https://rickandmortyapi.com/api/character/1"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kvaliteedijalg.backend")

rakendus = FastAPI(title=RAKENDUSE_NIMI, version="0.2.0")

rakendus.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def hanki_andmed(url: str) -> Dict[str, Any]:
    """Pärib välise API ja tagastab JSON andmed või viskab HTTP 502."""
    try:
        logger.info("Pärin välise API", extra={"siht": url})
        vastus = requests.get(url, timeout=5)
        vastus.raise_for_status()
        return vastus.json()

    except requests.RequestException as viga:
        logger.error("Välise API tõrge", exc_info=viga, extra={"siht": url})

        # Tagastame täpsemad 502 detailid
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
    """Kontrollib, kas backend töötab."""
    return {"olek": "aktiivne", "allikas": RAKENDUSE_NIMI}


@rakendus.get("/api/koond")
def koonda_andmed() -> Dict[str, Any]:
    """Kombineerib JSONPlaceholderi + Rick & Morty API vastused ühtsesse skeemi."""
    logger.info("Alustan koondpäringut")

    postitus = hanki_andmed(JSONPLACEHOLDER_URL)
    tegelane = hanki_andmed(RICK_MORTY_URL)

    logger.info(
        "Koondamine õnnestus",
        extra={"allikad": [JSONPLACEHOLDER_URL, RICK_MORTY_URL]},
    )

    paastiku_aeg = datetime.now(timezone.utc).isoformat()

    return {
        "postitus": {
            "id": postitus.get("id"),
            "pealkiri": postitus.get("title"),
            "katkend": (postitus.get("body") or "")[:120],
        },
        "tegelane": {
            "id": tegelane.get("id"),
            "nimi": tegelane.get("name"),
            "staatus": tegelane.get("status"),
        },
        "allikad": ["JSONPlaceholder", "Rick & Morty API"],
        "paastikuAeg": paastiku_aeg,
    }

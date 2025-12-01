"""Pytest näited FastAPI koondteenuse jaoks."""

from datetime import datetime
from typing import Any, Dict
from fastapi import HTTPException

import pytest
import requests
import time
from fastapi.testclient import TestClient

from backend.main import (
    JSONPLACEHOLDER_URL,
    RICK_MORTY_URL,
    hanki_andmed,
    rakendus,
)

client = TestClient(rakendus)


class MockResponse:
    """Lihtne mock, mis jäljendab requests.Response käitumist."""

    def __init__(self, json_keha: Dict[str, Any], status_code: int = 200):
        self._json_keha = json_keha
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise ValueError(f"HTTP {self.status_code}")

    def json(self) -> Dict[str, Any]:
        return self._json_keha

def test_status_endpoint_annab_aktiivse_oleku() -> None:
    vastus = client.get("/status")
    assert vastus.status_code == 200
    keha = vastus.json()
    assert keha["olek"] == "aktiivne"
    assert "Kvaliteedijälg" in keha["allikas"]


def test_hanki_andmed_tostab_vea(monkeypatch: pytest.MonkeyPatch) -> None:
    def _faux_get(*_args: Any, **_kwargs: Any) -> MockResponse:
        raise requests.RequestException("võrk maas")

    monkeypatch.setattr("requests.get", _faux_get)
    with pytest.raises(Exception):
        hanki_andmed("https://naidis.url")


def test_koond_endpoint_tagastab_pealkirja(monkeypatch: pytest.MonkeyPatch) -> None:
    def _valitud_get(url: str, *_args: Any, **_kwargs: Any) -> MockResponse:
        if url == JSONPLACEHOLDER_URL:
            return MockResponse({"id": 1, "title": "Test pealkiri", "body": "Sisu"})
        if url == RICK_MORTY_URL:
            return MockResponse({"id": 10, "name": "Rick", "status": "Alive"})
        raise ValueError("Ootamatu URL")

    monkeypatch.setattr("requests.get", _valitud_get)
    vastus = client.get("/api/koond")
    keha = vastus.json()

    assert keha["postitus"]["pealkiri"] == "Test pealkiri"
    assert keha["tegelane"]["nimi"] == "Rick"
    assert len(keha["allikad"]) == 2


def test_koond_endpoint_paiskiri_on_iso(monkeypatch: pytest.MonkeyPatch) -> None:
    def _valitud_get(url: str, *_args: Any, **_kwargs: Any) -> MockResponse:
        return MockResponse({"id": 1, "title": "X", "body": "Y"})  # mõlemale API-le

    monkeypatch.setattr("requests.get", _valitud_get)
    vastus = client.get("/api/koond")
    aeg = vastus.json()["paastikuAeg"]
    # Kontrolli, et ISO kuupäev parsitav
    datetime.fromisoformat(aeg)


def test_koond_endpoint_vigastab_allikaid(monkeypatch: pytest.MonkeyPatch) -> None:
    def _valitud_get(url: str, *_args: Any, **_kwargs: Any) -> MockResponse:
        if url == JSONPLACEHOLDER_URL:
            raise requests.RequestException("Katkestus")
        return MockResponse({"id": 2, "name": "Morty", "status": "Alive"})

    monkeypatch.setattr("requests.get", _valitud_get)
    vastus = client.get("/api/koond")
    assert vastus.status_code == 502

# Minu testid

# Kontrollib, et /api/koond vastab mõistliku aja jooksul (<2 sekundit)
def test_koond_endpoint_vastusaeg (monkeypatch):
    def _mock_get(url, *args, **kwargs):
        # Asendatav vastus mõlemale välisele API-le
        return MockResponse({"id": 1, "title": "X", "body": "Y"})
    monkeypatch.setattr("requests.get", _mock_get)
    algusaeg  = time.time()
    vastus  = client.get("/api/koond")
    kulunud  = time.time() - algusaeg 
    assert kulunud  < 2

# Kontrollib, et /api/koond tagastab õige pealkirja Content-Type.
def test_koond_endpoint_pealkirjad(monkeypatch):
    def _mock_get(url, *args, **kwargs):
        # Universaalne MockResponse mis tahes URL-ile
        return MockResponse({"id": 1, "title": "X", "body": "Y"})
    monkeypatch.setattr("requests.get", _mock_get)
    vastus  = client.get("/api/koond")
    # Kontrollime, et lõpppunkt tagastab JSON
    assert vastus .headers["content-type"] == "application/json"

# Kontrollib, et võrguvea korral visatakse välja HTTPException staatusega 502
def test_hanki_andmed_tundmatu_url(monkeypatch):
    # Simuleerime võrguvea
    def _mock_get(*args, **kwargs):
        raise requests.RequestException("Tundmatu URL")
    monkeypatch.setattr("requests.get", _mock_get)
    # Ootame HTTPException staatusega 502
    with pytest.raises(HTTPException) as veateade:
        hanki_andmed("https://unknown.url")
    assert veateade.value.status_code == 502

# Kontrollib, et funktsioon hanki_andmed kirjutab vea korral logisse sõnumi
def test_hanki_andmed_logging(monkeypatch, caplog):
    def _mock_get(*args, **kwargs):
        raise requests.RequestException("Võrk pole kättesaadav")
    monkeypatch.setattr("requests.get", _mock_get)
    # Kontrollime, kas logides ilmub veateade
    with pytest.raises(Exception):
        with caplog.at_level("INFO"):
            hanki_andmed("https://fake.url")
    assert "Võrk pole kättesaadav" in caplog.text
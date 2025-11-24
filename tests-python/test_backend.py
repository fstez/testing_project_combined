import pytest
from fastapi.testclient import TestClient
from backend.main import rakendus, hanki_andmed, JSONPLACEHOLDER_URL, RICK_MORTY_URL
from datetime import datetime
from unittest.mock import patch


client = TestClient(rakendus)


# 1) Edukas vastus /api/koond
def test_koond_success(monkeypatch):
    """Kontrollib, et API tagastab õige skeemi kui välised teenused töötavad."""

    def mock_jsonplaceholder(url):
        return {
            "id": 1,
            "title": "Test pealkiri",
            "body": "See on testikeha backend testimiseks."
        }

    def mock_rick(url):
        return {
            "id": 1,
            "name": "Rick Sanchez",
            "status": "Alive"
        }

    monkeypatch.setattr("backend.main.hanki_andmed", lambda url: mock_jsonplaceholder(url) if "jsonplaceholder" in url else mock_rick(url))

    vastus = client.get("/api/koond")
    assert vastus.status_code == 200

    keha = vastus.json()
    assert "postitus" in keha
    assert "tegelane" in keha
    assert "allikad" in keha
    assert "paastikuAeg" in keha


# 2) Veaolukord → HTTP 502
def test_koond_external_error(monkeypatch):
    """Kui väline teenus annab vea, tagastame 502."""

    def mock_fail(url):
        raise Exception("Test error")

    monkeypatch.setattr("backend.main.hanki_andmed", mock_fail)

    vastus = client.get("/api/koond")
    assert vastus.status_code == 502

    keha = vastus.json()
    assert keha["detail"]["sonum"] == "Välise teenuse tõrge"


# 3) Ajatempli formaat
def test_paastiku_aeg_format(monkeypatch):
    """Testib, et paastikuAeg on ISO kuupäev koos Z/UTC."""

    monkeypatch.setattr("backend.main.hanki_andmed", lambda url: {"id": 1, "title": "x", "body": "y"})
    
    vastus = client.get("/api/koond")
    aeg = vastus.json()["paastikuAeg"]

    # Kas on parseeritav?
    dt = datetime.fromisoformat(aeg.replace("Z", "+00:00"))
    assert isinstance(dt, datetime)


# 4) Skeem: postitus ja tegelane sisaldavad nõutud välju
def test_schema_fields(monkeypatch):
    """Kontrollib, et skeemi struktuur on õige."""

    monkeypatch.setattr(
        "backend.main.hanki_andmed",
        lambda url: {"id": 1, "title": "T", "body": "B"} if "jsonplaceholder" in url else {"id": 5, "name": "Rick", "status": "Alive"}
    )

    vastus = client.get("/api/koond")
    keha = vastus.json()

    assert set(keha["postitus"].keys()) == {"id", "pealkiri", "katkend"}
    assert set(keha["tegelane"].keys()) == {"id", "nimi", "staatus"}


# 5) Logi väljakutse → logger.info / logger.error
def test_logging_called(monkeypatch):
    """Kontrollib, et koondamisel logitakse."""

    called_messages = []

    def mock_info(msg, *args, **kwargs):
        called_messages.append(msg)

    monkeypatch.setattr("backend.main.logger.info", mock_info)
    monkeypatch.setattr("backend.main.hanki_andmed", lambda url: {"id": 1})

    client.get("/api/koond")

    assert any("Koondan API vastuseid" in msg or "Koondamine" in msg for msg in called_messages)

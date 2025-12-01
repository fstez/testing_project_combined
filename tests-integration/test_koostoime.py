"""Integratsioonitestid, mis kasutavad päris FastAPI rakendust ja mockitud väliseid teenuseid."""

from fastapi.testclient import TestClient
import pytest
import responses

from backend.main import JSONPLACEHOLDER_URL, RICK_MORTY_URL, rakendus

client = TestClient(rakendus)


@responses.activate
def test_koond_endpoint_onnestub_kui_valised_teenused_toimivad(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level("INFO")
    responses.add(
        responses.GET,
        JSONPLACEHOLDER_URL,
        json={"id": 1, "title": "Integratsioon", "body": "pikem tekst"},
        status=200,
    )
    responses.add(
        responses.GET,
        RICK_MORTY_URL,
        json={"id": 42, "name": "Morty Smith", "status": "Alive"},
        status=200,
    )

    vastus = client.get("/api/koond")

    assert vastus.status_code == 200
    keha = vastus.json()
    assert keha["postitus"]["pealkiri"] == "Integratsioon"
    assert keha["tegelane"]["nimi"] == "Morty Smith"
    assert JSONPLACEHOLDER_URL in keha["allikad"]
    assert RICK_MORTY_URL in keha["allikad"]
    assert any("Koondan API vastuseid" in rekord.message for rekord in caplog.records)


@responses.activate
def test_koond_endpoint_annab_502_kui_valis_api_katkestab() -> None:
    responses.add(
        responses.GET,
        JSONPLACEHOLDER_URL,
        status=500,
    )
    responses.add(
        responses.GET,
        RICK_MORTY_URL,
        body=responses.ConnectionError("võrguviga"),
    )

    vastus = client.get("/api/koond")
    assert vastus.status_code == 502
    keha = vastus.json()
    assert keha["detail"]["sonum"] == "Välise teenuse tõrge"
    assert keha["detail"]["siht"] in (JSONPLACEHOLDER_URL, RICK_MORTY_URL)


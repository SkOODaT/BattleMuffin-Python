import os
from battlemuffin.clients.warcraft_client import WarcraftClient


def test_get_realms_index(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_realms_index()
    assert response == snapshot


def test_get_realm(snapshot):
    client = WarcraftClient(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
    response = client.get_realm(1)
    assert response == snapshot

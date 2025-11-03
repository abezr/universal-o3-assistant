"""Tests for the FastAPI health endpoint."""
from fastapi.testclient import TestClient

from uda.api import app


def test_health_endpoint_returns_ok_status() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

import pytest
from fastapi.testclient import TestClient

from main import app


class TestClinicAPI:

    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_health_endpoint(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_get_appointments(self, client):
        response = client.get("/appointments")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "id" in data[0]
        assert "patient_name" in data[0]

    def test_nonexistent_endpoint(self, client):
        response = client.get("/nonexistent")
        assert response.status_code == 404

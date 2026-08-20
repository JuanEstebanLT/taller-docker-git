from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "API CI/CD funcionando",
        "version": "1.0.0"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_info():
    response = client.get("/info")

    assert response.status_code == 200

    data = response.json()

    assert data["aplicacion"] == "API FastAPI CI/CD"
    assert data["version"] == "1.0.0"
    assert data["entorno"] == "Docker"


def test_ruta_inexistente():
    response = client.get("/ruta-que-no-existe")

    assert response.status_code == 404
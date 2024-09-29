import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_get_producao():
    response = client.get("/producao")
    assert response.status_code == 200
    assert response.json() is not None
    client = TestClient(app)

def test_get_producao():
    response = client.get("/producao")
    assert response.status_code == 200
    assert response.json() is not None

def test_get_processamento():
    response = client.get("/processamento")
    assert response.status_code == 200
    assert response.json() is not None

def test_get_comercializacao():
    response = client.get("/comercializacao")
    assert response.status_code == 200
    assert response.json() is not None

def test_get_importacao():
    response = client.get("/importacao")
    assert response.status_code == 200
    assert response.json() is not None

def test_get_exportacao():
    response = client.get("/exportacao")
    assert response.status_code == 200
    assert response.json() is not None

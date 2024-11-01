import pytest
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_get_producao():
    response = client.get("/producao")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_viniferas():
    response = client.get("/processamento_viniferas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_americanas():
    response = client.get("/processamento_americanas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_mesa():
    response = client.get("/processamento_mesa")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_sem_classi():
    response = client.get("/processamento_sem_classi")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_comercializacao():
    response = client.get("/comercializacao")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_vinhos():
    response = client.get("/importacao_vinhos")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_espumantes():
    response = client.get("/importacao_espumantes")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_uvas():
    response = client.get("/importacao_uvas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_passas():
    response = client.get("/importacao_passas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_suco():
    response = client.get("/importacao_suco")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_vinho():
    response = client.get("/exportacao_vinho")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_espumante():
    response = client.get("/exportacao_espumante")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_uva():
    response = client.get("/exportacao_uva")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_suco():
    response = client.get("/exportacao_suco")
    assert response.status_code == 401
    assert response.json() is not None

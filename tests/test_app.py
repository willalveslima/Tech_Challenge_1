import pytest
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_get_producao():
    response = client.get("/producao")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_viniferas():
    response = client.get("/processamento/viniferas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_americanas():
    response = client.get("/processamento/americanas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_mesa():
    response = client.get("/processamento/mesa")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_processamento_sem_classi():
    response = client.get("/processamento/sem_classi")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_comercializacao():
    response = client.get("/comercializacao")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_vinhos():
    response = client.get("/importacao/vinhos")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_espumantes():
    response = client.get("/importacao/espumantes")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_uvas():
    response = client.get("/importacao/uvas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_passas():
    response = client.get("/importacao/passas")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_importacao_suco():
    response = client.get("/importacao/suco")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_vinho():
    response = client.get("/exportacao/vinho")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_espumante():
    response = client.get("/exportacao/espumante")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_uva():
    response = client.get("/exportacao/uva")
    assert response.status_code == 401
    assert response.json() is not None

def test_get_exportacao_suco():
    response = client.get("/exportacao/suco")
    assert response.status_code == 401
    assert response.json() is not None

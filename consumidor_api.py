"""Modelo de consumidor de API com autenticação JWT."""
import json

import requests

# URL para obter o token JWT
auth_url = "http://127.0.0.1:8000/token"

# Credenciais do usuário
username = "johndoe"
password = "fakehashedpassword"

# Dados para a requisição de autenticação
auth_data = {
    "username": username,
    "password": password
}

# Fazendo a requisição POST para obter o token JWT
auth_response = requests.post(auth_url, data=auth_data)
print(auth_response)
# Verificando o status da resposta de autenticação
if auth_response.status_code == 200:
    # Sucesso na autenticação
    token = auth_response.json().get("token")
    print(f"Token: {token}")
    # URL da API
    url = "http://127.0.0.1:8000/producao"

    # Cabeçalhos da requisição
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Fazendo a requisição GET
    response = requests.get(url, headers=headers)

    # Verificando o status da resposta
    if response.status_code == 200:
        # Sucesso
        data = response.json()
        print(data)
    else:
        # Falha
        print(f"Erro {response.status_code}: {response.text}")
else:
    # Falha na autenticação
    print(f"Erro {auth_response.status_code}: {auth_response.text}")
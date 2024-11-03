"""Exemplo de consumidor da API Rodando localmente."""

import pandas as pd
import requests

print("\nIniciando a execução...")

# URLs das APIs
lista = [
    "producao",
    "processamento/viniferas",
    "processamento/americanas",
    "processamento/mesa",
    "processamento/sem_classi",
    "comercializacao",
    "importacao/vinhos",
    "importacao/espumantes",
    "importacao/uvas",
    "importacao/passas",
    "importacao/suco",
    "exportacao/vinho",
    "exportacao/espumante",
    "exportacao/uva",
    "exportacao/suco",
]


URL = "http://127.0.0.1:8000/"

# Função para obter o token JWT


def obter_token(email, senha):
    """Obtém o token JWT."""
    url_signin = URL + "/users/signin"
    payload = {"username": email, "password": senha}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url_signin, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Erro ao obter token: {response.status_code} {response.text}")
        return None

# Função para criar usuário


def criar_usuario(nome, email, senha):
    """Cria um usuário."""
    url_signup = URL + "users/signup"
    payload = {
        "name": nome,
        "email": email,
        "password": senha}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url_signup, json=payload, headers=headers)

    if response.status_code == 201:
        print("Usuário criado com sucesso.")
    else:
        print(f"Erro ao criar usuário: {response.status_code} {response.text}")


nome = "consumidor_teste"
email = "consumidor@teste.com"
senha = "senha123"

token = obter_token(email, senha)
if not token:
    print("Usuário não encontrado. Criando usuário...")
    criar_usuario(nome, email, senha)
    token = obter_token(email, senha)
if token:
    headers = {"Authorization": f"Bearer {token}"}
    for endpoint in lista:
        print(f"Consultando base {endpoint}")
        print(f"URL: {URL + endpoint}")

        try:
            # Fazendo a requisição GET para a API
            response = requests.get(
                URL + endpoint,  headers=headers, timeout=30)

            # Verificando se a requisição foi bem-sucedida
            if response.status_code == 200:
                # Convertendo a resposta JSON em um DataFrame
                data = response.json()
                print(type(data))

                df = pd.DataFrame(data)

                # Exibindo o head do DataFrame
                print(df.head(10))

            else:
                print(
                    f"Erro ao acessar a API: {response.status_code} \
                        {response.text}")
            print("*" * 80 + "\n")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}")
            print("*" * 80 + "\n")
else:
    print("Erro ao obter token.")
print("Fim da execução.")
print("*" * 80)
print()

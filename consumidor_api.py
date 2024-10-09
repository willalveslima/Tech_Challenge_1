"""Exemplo de consumidor da API Rodando localmente."""

import pandas as pd
import requests

# URLs das APIs
lista = [
    "producao",
    "processamento_viniferas",
    "processamento_americanas",
    "processamento_mesa",
    "processamento_sem_classi",
    "comercializacao",
    "importacao_vinhos",
    "importacao_espumantes",
    "importacao_uvas",
    "importacao_passas",
    "importacao_suco",
    "exportacao_vinho",
    "exportacao_espumante",
    "exportacao_uva",
    "exportacao_suco",
]

URL = "http://127.0.0.1:8000/"


for endpoint in lista:
    print(f"Consultando base {endpoint}")
    print(f"URL: {URL + endpoint}")

    try:
        # Fazendo a requisição GET para a API
        response = requests.get(URL + endpoint, timeout=10)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Convertendo a resposta JSON em um DataFrame
            data = response.json()
            df = pd.read_json(data)

            # Exibindo o head do DataFrame
            print(df.head())
        else:
            print(
                f"Erro ao acessar a API: {response.status_code} \
                    {response.text}")
        print("*" * 80 + "\n")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        print("*" * 80 + "\n")

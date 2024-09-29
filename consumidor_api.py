"""Exemplo de consumidor da API."""
import pandas as pd
import requests

# URLs das APIs
lista = ["producao", "processamento",
         "comercializacao", "importacao", "exportacao"]
url = 'http://127.0.0.1:8000/'


for endpoint in lista:

    # Fazendo a requisição GET para a API
    response = requests.get(url + endpoint)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta JSON em um DataFrame
        data = response.json()
        df = pd.read_json(data)

        # Exibindo o head do DataFrame
        print(df.head())
    else:
        print(f"Erro ao acessar a API: {response.status_code} {response.text}")

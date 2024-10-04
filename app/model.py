import pandas as pd
from enum import Enum
from fastapi import HTTPException
import csv
import requests
from io import StringIO
from app.tratamento import TratamentoColunaAnoSimples,TratamentoColunaAnoDuplo

URL_BASE_PRODUCAO = "http://127.0.0.1/Producao.csv"
# URL_BASE_PRODUCAO = (
# "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")


class BASE(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (URL_BASE_PRODUCAO, "Base de Produção", TratamentoColunaAnoSimples())
    PROCESSAMENTO_VINIFERAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento Viniferas",TratamentoColunaAnoSimples())
    PROCESSAMENTO_AMERICANAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "Base de Processamento Americanas",TratamentoColunaAnoSimples())
    PROCESSAMENTO_MESA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "Base de Processamento Uvas de Mesa",TratamentoColunaAnoSimples())
    PROCESSAMENTO_SEM_CLASSI = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "Base de Sem Classificação",TratamentoColunaAnoSimples())
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização",TratamentoColunaAnoSimples())
    IMPORTACAO_VINHOS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação Vinhos de Mesa",TratamentoColunaAnoDuplo())
    IMPORTACAO_ESPUMANTES = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "Base de Importação Espumantes",TratamentoColunaAnoDuplo())
    IMPORTACAO_UVAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "Base de Importação Uvas Frescas",TratamentoColunaAnoDuplo())
    IMPORTACAO_PASSAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "Base de Importação Uvas Passas",TratamentoColunaAnoDuplo())
    IMPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "Base de Importação Suco de uva",TratamentoColunaAnoDuplo())

    EXPORTACAO_VINHO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação Vinho de Mesa", TratamentoColunaAnoDuplo())

    EXPORTACAO_ESPUMANTE = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "Base de Exportação Espumante", TratamentoColunaAnoDuplo())

    EXPORTACAO_UVA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "Base de Exportação Uvas Frescas", TratamentoColunaAnoDuplo())

    EXPORTACAO_SUCO = (
        "http://127.0.0.1/ExpSuco.csv",
        "Base de Exportação Suco de Uva", TratamentoColunaAnoDuplo())

    def __init__(self, url, descricao, tratamento):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.tratamento = tratamento


class Consultar:
    def __init__(self, base: BASE):
        self.base = base
        self.df = None

    def detect_separator(self, sample: str) -> str:
        try:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            return dialect.delimiter
        except csv.Error:
            # Fallback para delimitadores comuns
            common_delimiters = [',', ';', '\t']
            for delimiter in common_delimiters:
                if delimiter in sample:
                    return delimiter
            raise ValueError("Could not determine delimiter")

    def executa(self):
        try:
            # Baixar uma amostra do arquivo
            response = requests.get(self.base.url)
            response.raise_for_status()
            sample = response.text[:5000]  # Lê os primeiros 1024 caracteres

            # Detectar o separador
            sep = self.detect_separator(sample)


            # Ler o arquivo completo com o separador detectado
            self.df = pd.read_csv(StringIO(response.text), sep=sep, on_bad_lines='warn')
            if self.base.tratamento is not None:
                self.df = self.base.tratamento.tratar(self.df)
            return self.df.to_json(orient="records")
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao ao consultar a {self.base.descricao}, tente novamente mais tarde. {str(e)}",
            )

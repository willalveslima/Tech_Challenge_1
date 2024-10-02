import pandas as pd
from enum import Enum
from fastapi import HTTPException
from app.tratamento import TratamentoProducao

URL_BASE_PRODUCAO = "http://127.0.0.1/Producao.csv"
# URL_BASE_PRODUCAO = (
# "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")


class BASE2(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (URL_BASE_PRODUCAO, "Base de Produção", TratamentoProducao())
    PROCESSAMENTO_VINIFERAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento Viniferas",None)
    PROCESSAMENTO_AMERICANAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "Base de Processamento Americanas",None)
    PROCESSAMENTO_MESA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "Base de Processamento Uvas de Mesa",None)
    PROCESSAMENTO_SEM_CLASSI = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "Base de Sem Classificação",None)
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização",None)
    IMPORTACAO_VINHOS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação Vinhos de Mesa",None)
    IMPORTACAO_ESPUMANTES = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "Base de Importação Espumantes",None)
    IMPORTACAO_UVAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "Base de Importação Uvas Frescas",None)
    IMPORTACAO_PASSAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "Base de Importação Uvas Passas",None)
    IMPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "Base de Importação Suco de uva",None)

    EXPORTACAO_VINHO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação Vinho de Mesa", None)
    
    EXPORTACAO_ESPUMANTE = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "Base de Exportação Espumante", None)

    EXPORTACAO_UVA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "Base de Exportação Uvas Frescas", None)

    EXPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "Base de Exportação Suco de Uva", None)

    def __init__(self, url, descricao, tratamento):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.tratamento = tratamento


class Consultar():
    def __init__(self, base: BASE2):
        self.base = base
        self.df = None
    def executa(self):
        try:
            self.df = pd.read_csv(self.base.url, sep=";")
            if self.base.tratamento is not None:
                self.df = self.base.tratamento.tratar(self.df)
            return self.df.to_json(orient="records")    
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao ao consultar a {self.base.descricao}: {str(e)}",
            )

        
    


"""Constantes utilizadas no projeto."""
from enum import Enum

# URLS dos arquivos CSV
# URL_BASE_PRODUCAO =
# "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
URL_BASE_PROCESSAMENTO = (
    "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
)
URL_BASE_COMERCIALIZACAO = (
    "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv")
URL_BASE_IMPORTACAO = (
    "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv")
URL_BASE_EXPORTACAO = (
    "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv")

# URL teste
URL_BASE_PRODUCAO = "http://127.0.0.1/Producao.csv"


class BASE(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (URL_BASE_PRODUCAO, "Base de Produção")
    PROCESSAMENTO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento")
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização")
    IMPORTACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação")
    EXPORTACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação")

    def __init__(self, url, descricao):
        """Construtor."""
        self.url = url
        self.descricao = descricao

"""Informações das Bases de dados e módulo de Consulta."""

import io
import logging
from enum import Enum

import pandas as pd
from fastapi import HTTPException
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_cache import CachedSession

from app.formata_dfs import FormataColunaAnoDuplo, FormataColunaAnoSimples

logger = logging.getLogger("main.app.model")

retry_strategy = Retry(
    total=30,
    status_forcelist=[429, 500, 502, 503, 504],
    backoff_factor=0.1,

)
adapter = HTTPAdapter(max_retries=retry_strategy)


class BASE(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "Base de Produção",
        ";",
        FormataColunaAnoSimples(),
    )
    PROCESSAMENTO_VINIFERAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento Viniferas",
        ";",
        FormataColunaAnoSimples(),
    )
    PROCESSAMENTO_AMERICANAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "Base de Processamento Americanas",
        "\t",
        FormataColunaAnoSimples(),
    )
    PROCESSAMENTO_MESA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "Base de Processamento Uvas de Mesa",
        "\t",
        FormataColunaAnoSimples(),
    )
    PROCESSAMENTO_SEM_CLASSI = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "Base de Sem Classificação",
        "\t",
        FormataColunaAnoSimples(),
    )
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização",
        ";",
        FormataColunaAnoSimples(),
    )
    IMPORTACAO_VINHOS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação Vinhos de Mesa",
        ";",
        FormataColunaAnoDuplo(),
    )
    IMPORTACAO_ESPUMANTES = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "Base de Importação Espumantes",
        ";",
        FormataColunaAnoDuplo(),
    )
    IMPORTACAO_UVAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "Base de Importação Uvas Frescas",
        ";",
        FormataColunaAnoDuplo(),
    )
    IMPORTACAO_PASSAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "Base de Importação Uvas Passas",
        ";",
        FormataColunaAnoDuplo(),
    )
    IMPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "Base de Importação Suco de uva",
        ";",
        FormataColunaAnoDuplo(),
    )

    EXPORTACAO_VINHO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação Vinho de Mesa",
        ";",
        FormataColunaAnoDuplo(),
    )

    EXPORTACAO_ESPUMANTE = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "Base de Exportação Espumante",
        ";",
        FormataColunaAnoDuplo(),
    )

    EXPORTACAO_UVA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "Base de Exportação Uvas Frescas",
        ";",
        FormataColunaAnoDuplo(),
    )

    EXPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "Base de Exportação Suco de Uva",
        ";",
        FormataColunaAnoDuplo(),
    )

    def __init__(self, url, descricao, sep, formatacao):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.sep = sep
        self.formatacao = formatacao


class Consultar:
    """Classe Consultar."""

    def __init__(self, base: BASE):
        """Construtor."""
        self.base = base
        self.df = None

    def executa(self):
        """Executa a consulta das Bases."""
        logger.debug("Consultar.executa(): Acessando url: %s", self.base.url)
        try:

            http = CachedSession(expire_after=36000)
            http.mount("http://", adapter)
            http.headers.update({"User-Agent": "Mozilla/5.0"})
            response = http.get(self.base.url, timeout=30, stream=True)
            if response.status_code != 200:
                logger.error("%s Consulta falhou.", response.status_code)
                raise HTTPException(
                    status_code=500,
                    detail=f"Erro ao acessar a URL {self.base.url}.",
                )
            csv = response.content

            self.df = pd.read_csv(io.StringIO(csv.decode('utf-8')),
                                  sep=self.base.sep)
            if self.base.formatacao is not None:
                self.df = self.base.formatacao.formatar(self.df)
            logger.debug(
                "Consultar.executa(): Consulta realizada com sucesso." +
                "Retornando JSON."
            )
            return self.df.to_json(orient="records")
        except Exception as e:
            logger.error(str(e))
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao ao consultar a {self.base.descricao}," +
                "tente novamente mais tarde.",
            ) from e

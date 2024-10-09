"""Informações das Bases de dados e módulo de Consulta."""

import logging
from enum import Enum

import pandas as pd
from fastapi import HTTPException

from app.tratamento import TratamentoColunaAnoDuplo, TratamentoColunaAnoSimples

logger = logging.getLogger("main.app.model")


class BASE(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "Base de Produção",
        ";",
        TratamentoColunaAnoSimples(),
    )
    PROCESSAMENTO_VINIFERAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento Viniferas",
        ";",
        TratamentoColunaAnoSimples(),
    )
    PROCESSAMENTO_AMERICANAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "Base de Processamento Americanas",
        "\t",
        TratamentoColunaAnoSimples(),
    )
    PROCESSAMENTO_MESA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "Base de Processamento Uvas de Mesa",
        "\t",
        TratamentoColunaAnoSimples(),
    )
    PROCESSAMENTO_SEM_CLASSI = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "Base de Sem Classificação",
        "\t",
        TratamentoColunaAnoSimples(),
    )
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização",
        ";",
        TratamentoColunaAnoSimples(),
    )
    IMPORTACAO_VINHOS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação Vinhos de Mesa",
        ";",
        TratamentoColunaAnoDuplo(),
    )
    IMPORTACAO_ESPUMANTES = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "Base de Importação Espumantes",
        ";",
        TratamentoColunaAnoDuplo(),
    )
    IMPORTACAO_UVAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "Base de Importação Uvas Frescas",
        ";",
        TratamentoColunaAnoDuplo(),
    )
    IMPORTACAO_PASSAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "Base de Importação Uvas Passas",
        ";",
        TratamentoColunaAnoDuplo(),
    )
    IMPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "Base de Importação Suco de uva",
        ";",
        TratamentoColunaAnoDuplo(),
    )

    EXPORTACAO_VINHO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação Vinho de Mesa",
        ";",
        TratamentoColunaAnoDuplo(),
    )

    EXPORTACAO_ESPUMANTE = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "Base de Exportação Espumante",
        ";",
        TratamentoColunaAnoDuplo(),
    )

    EXPORTACAO_UVA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "Base de Exportação Uvas Frescas",
        ";",
        TratamentoColunaAnoDuplo(),
    )

    EXPORTACAO_SUCO = (
        "http://127.0.0.1/ExpSuco.csv",
        "Base de Exportação Suco de Uva",
        ";",
        TratamentoColunaAnoDuplo(),
    )

    def __init__(self, url, descricao, sep, tratamento):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.sep = sep
        self.tratamento = tratamento


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

            self.df = pd.read_csv(self.base.url, sep=self.base.sep)
            if self.base.tratamento is not None:
                self.df = self.base.tratamento.tratar(self.df)
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

"""Informações das Bases de dados e módulo de Consulta."""

import io
import logging
import os
from enum import Enum

import numpy as np
import pandas as pd
from fastapi import HTTPException
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests_cache import CachedSession

from app.schemas.bases import (Comercializacao, Exportacao, Importacao,
                               Processamento, Producao)
from app.utils.formata_dfs import (FormataColunaAnoDuplo,
                                   FormataColunaAnoSimples)

logger = logging.getLogger("main.app.services.consulta_bases")

TIMEOUT = int(os.getenv("TIMEOUT", 30))
CACHE_NAME = os.getenv("CACHE_NAME", 'storage/app/http_cache')
CACHE_EXPIRES = int(os.getenv("CACHE_EXPIRES", 172800))

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
        "Produção de vinhos, sucos e derivados do Rio Grande do Sul",
        "CONTROL: Tipo, PRODUTO: Especificação, ANO: Ano de produção e L: "
        "QTD em Litros",
        ";",
        FormataColunaAnoSimples(),
        Producao,
    )
    PROCESSAMENTO_VINIFERAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Quantidade de uvas Viniferas processadas no Rio Grande do Sul",
        "CONTROL: Tipo, CULTIVAR: Especificação, ANO: Ano de processamento e "
        "Kg: QTD em Kilos",
        ";",
        FormataColunaAnoSimples(),
        Processamento,
    )
    PROCESSAMENTO_AMERICANAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "Quantidade de uvas Americanas e Hibridas processadas no "
        "Rio Grande do Sul",
        "CONTROL: Tipo, CULTIVAR: Especificação, ANO: Ano de processametno e "
        "Kg: QTD em Kilos",
        "\t",
        FormataColunaAnoSimples(),
        Processamento,
    )
    PROCESSAMENTO_MESA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "Quantidade de uva de Mesas processadas no Rio Grande do Sul",
        "CONTROL: Tipo, CULTIVAR: Especificação, ANO: Ano de processamento e "
        "Kg: QTD em Kilos",
        "\t",
        FormataColunaAnoSimples(),
        Processamento,
    )
    PROCESSAMENTO_SEM_CLASSI = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "Quantidade de uva Sem Classificação processadas no "
        "Rio Grande do Sul",
        "CONTROL: Tipo, CULTIVAR: Especificação, ANO: Ano de processamento e "
        "Kg: QTD em Kilos",
        "\t",
        FormataColunaAnoSimples(),
        Processamento,
    )
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Comercialização de vinhos e derivados no Rio Grande do Sul",
        "CONTROL: Tipo, PRODUTO: Especificação, ANO: Ano de Comercialização e"
        "L: QTD em Litros",
        ";",
        FormataColunaAnoSimples(),
        Comercializacao,
    )
    IMPORTACAO_VINHOS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        (
            "Importação de derivados de uva: Vinhos de mesa"
        ),
        (
            "País: País de Origem, ANO: Ano de Importação, Kg: QTD em Kilos, "
            "USD: Valor em US$"
        ),
        ";",
        FormataColunaAnoDuplo(),
        Importacao,
    )
    IMPORTACAO_ESPUMANTES = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "Importação de derivados de uva: Espumantes",
        (
            "País: País de Origem, ANO: Ano de Importação, Kg: QTD em Kilos, "
            "USD: Valor em US$"
        ),
        ";",
        FormataColunaAnoDuplo(),
        Importacao,
    )
    IMPORTACAO_UVAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "Importação de derivados de uva: Uvas Frescas",
        "País: País de Origem, ANO: Ano de Importação, Kg: QTD em Kilos, "
        "USD: Valor em US$",
        ";",
        FormataColunaAnoDuplo(),
        Importacao,
    )
    IMPORTACAO_PASSAS = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "Importação de derivados de uva: Uvas passas",
        (
            "País: País de Origem, ANO: Ano de Importação, Kg: QTD em Kilos, "
            "USD: Valor em US$"
        ),
        ";",
        FormataColunaAnoDuplo(),
        Importacao,
    )
    IMPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "Importação de derivados de uva: Suco de uva",
        (
            "País: País de Origem, ANO: Ano de Importação, Kg: QTD em Kilos, "
            "USD: Valor em US$"
        ),
        ";",
        FormataColunaAnoDuplo(),
        Importacao,
    )

    EXPORTACAO_VINHO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Exportação de derivados de uva: Vinho de mesa",
        "País: País de Destino, ANO: Ano da Exportação, Kg: QTD em Kilos, "
        "USD: Valor em US$",
        ";",
        FormataColunaAnoDuplo(),
        Exportacao,
    )

    EXPORTACAO_ESPUMANTE = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "Exportação de derivados de uva: Espumante",
        "País: País de Destino, ANO: Ano da Exportação, Kg: QTD em Kilos, "
        "USD: Valor em US$",
        ";",
        FormataColunaAnoDuplo(),
        Exportacao,
    )

    EXPORTACAO_UVA = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "Exportação de derivados de uva: Uvas Frescas",
        (
            "País: País de Destino, ANO: Ano da Exportação, Kg: QTD em Kilos, "
            "USD: Valor em US$"
        ),
        ";",
        FormataColunaAnoDuplo(),
        Exportacao,
    )

    EXPORTACAO_SUCO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "Exportação de derivados de uva: Suco de uva",
        "País: País de Destino, ANO: Ano da Exportação, Kg: QTD em Kilos, "
        "USD: Valor em US$",
        ";",
        FormataColunaAnoDuplo(),
        Exportacao,
    )

    def __init__(self, url, descricao, colunas, sep, formatacao,
                 response_model):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.colunas = colunas
        self.sep = sep
        self.formatacao = formatacao
        self.response_model = response_model


def forma_descricao(base: BASE) -> str:
    """Formata a descrição da base."""
    return (
        f'Consulta a base de dados Embrapa de {base.descricao} <br>'
        f'Disponível em {base.url} <br>'
        f'Retorno: Tabela Json com as colunas: {base.colunas}'
    )


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

            http = CachedSession(cache_name=CACHE_NAME,
                                 expire_after=CACHE_EXPIRES)
            http.mount("http://", adapter)
            http.headers.update({"User-Agent": "Mozilla/5.0"})
            response = http.get(self.base.url, timeout=TIMEOUT, stream=True)
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
            self.df.replace({np.nan: None}, inplace=True)
            logger.debug(
                "Consultar.executa(): Consulta realizada com sucesso." +
                "Retornando dict."
            )
            return self.df.to_dict('records')
        except Exception as e:
            logger.error(str(e))
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao ao consultar a {self.base.descricao}," +
                "tente novamente mais tarde.",
            ) from e

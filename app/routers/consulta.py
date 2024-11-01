"""API simples."""

import logging
from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar
from fastapi import APIRouter, Depends

consulta = APIRouter()


logger = logging.getLogger("main.app.router.consulta")


@consulta.get(
    "/producao",
    summary=BASE.PRODUCAO.descricao,
    description="Consulta a Base de Produção de vinhos da Empraba "
    + "e retorna os dados em formato JSON.",
)
async def get_producao(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Produção."""
    logger.debug("Chamada /producao - funcao get_producao")
    consulta = Consultar(BASE.PRODUCAO)
    return consulta.executa()


@consulta.get("/processamento_viniferas",
              summary=BASE.PROCESSAMENTO_VINIFERAS.descricao)
async def processamento_viniferas(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Processamento de Viníferas."""
    logger.debug(
        "Chamada /processamento_viniferas - funcao processamento_viniferas")
    consulta = Consultar(BASE.PROCESSAMENTO_VINIFERAS)
    return consulta.executa()


@consulta.get(
    "/processamento_americanas",
    summary=BASE.PROCESSAMENTO_AMERICANAS.descricao,
    description=(
        "Consulta a Base de Processamento Americanas \
            e retorna os dados em formato JSON."),
)
async def processamento_americanas(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Processamento Americanas."""
    logger.debug(
        "Chamada /processamento_americanas - funcao processamento_americanas")
    consulta = Consultar(BASE.PROCESSAMENTO_AMERICANAS)
    return consulta.executa()


@consulta.get(
    "/processamento_mesa",
    summary=BASE.PROCESSAMENTO_MESA.descricao,
    description="Consulta a Base de Processamento Uvas de Mesa \
        e retorna os dados em formato JSON.",
)
async def processamento_mesa(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Processamento Uvas de Mesa."""
    logger.debug("Chamada /processamento_mesa - funcao processamento_mesa")
    consulta = Consultar(BASE.PROCESSAMENTO_MESA)
    return consulta.executa()


@consulta.get(
    "/processamento_sem_classi",
    summary=BASE.PROCESSAMENTO_SEM_CLASSI.descricao,
    description="Consulta a Base de Sem Classificação \
        e retorna os dados em formato JSON.",
)
async def processamento_sem_classi(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Sem Classificação."""
    logger.debug(
        "Chamada /processamento_sem_classi - funcao processamento_sem_classi")
    consulta = Consultar(BASE.PROCESSAMENTO_SEM_CLASSI)
    return consulta.executa()


@consulta.get(
    "/comercializacao",
    summary=BASE.COMERCIALIZACAO.descricao,
    description="Consulta a Base de Comercialização e \
        retorna os dados em formato JSON.",
)
async def comercializacao(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Comercialização."""
    logger.debug("Chamada /comercializacao - funcao comercializacao")
    consulta = Consultar(BASE.COMERCIALIZACAO)
    return consulta.executa()


@consulta.get(
    "/importacao_vinhos",
    summary=BASE.IMPORTACAO_VINHOS.descricao,
    description="Consulta a Base de Importação Vinhos de Mesa e \
        retorna os dados em formato JSON.",
)
async def importacao_vinhos(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Importação Vinhos de Mesa."""
    logger.debug("Chamada /importacao_vinhos - funcao importacao_vinhos")
    consulta = Consultar(BASE.IMPORTACAO_VINHOS)
    return consulta.executa()


@consulta.get(
    "/importacao_espumantes",
    summary=BASE.IMPORTACAO_ESPUMANTES.descricao,
    description="Consulta a Base de Importação Espumantes \
        e retorna os dados em formato JSON.",
)
async def importacao_espumantes(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Importação Espumantes."""
    logger.debug(
        "Chamada /importacao_espumantes - funcao importacao_espumantes")
    consulta = Consultar(BASE.IMPORTACAO_ESPUMANTES)
    return consulta.executa()


@consulta.get(
    "/importacao_uvas",
    summary=BASE.IMPORTACAO_UVAS.descricao,
    description="Consulta a Base de Importação Uvas Frescas \
        e retorna os dados em formato JSON.",
)
async def importacao_uvas(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Importação Uvas Frescas."""
    logger.debug("Chamada /importacao_uvas - funcao importacao_uvas")
    consulta = Consultar(BASE.IMPORTACAO_UVAS)
    return consulta.executa()


@consulta.get(
    "/importacao_passas",
    summary=BASE.IMPORTACAO_PASSAS.descricao,
    description="Consulta a Base de Importação Uvas Passas \
        e retorna os dados em formato JSON.",
)
async def importacao_passas(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Importação Uvas Passas."""
    logger.debug("Chamada /importacao_passas - funcao importacao_passas")
    consulta = Consultar(BASE.IMPORTACAO_PASSAS)
    return consulta.executa()


@consulta.get(
    "/importacao_suco",
    summary=BASE.IMPORTACAO_SUCO.descricao,

    description="Consulta a Base de Importação Suco de uva \
        e retorna os dados em formato JSON.",
)
async def importacao_suco(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Importação Suco de uva."""
    logger.debug("Chamada /importacao_suco - funcao importacao_suco")
    consulta = Consultar(BASE.IMPORTACAO_SUCO)
    return consulta.executa()


@consulta.get(
    "/exportacao_vinho",
    summary=BASE.EXPORTACAO_VINHO.descricao,
    description="Consulta a Base de Exportação Vinho de Mesa e \
        retorna os dados em formato JSON.",
)
async def exportacao_vinho(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Exportação Vinho de Mesa."""
    logger.debug("Chamada /exportacao_vinho - funcao exportacao_vinho")
    consulta = Consultar(BASE.EXPORTACAO_VINHO)
    return consulta.executa()


@consulta.get(
    "/exportacao_espumante",
    summary=BASE.EXPORTACAO_ESPUMANTE.descricao,
    description=(
        "Consulta a Base de Exportação Espumante \
            e retorna os dados em formato JSON."
    ),
)
async def exportacao_espumante(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Exportação Espumante."""
    logger.debug("Chamada /exportacao_espumante - funcao exportacao_espumante")
    consulta = Consultar(BASE.EXPORTACAO_ESPUMANTE)
    return consulta.executa()


@consulta.get(
    "/exportacao_uva",
    summary=BASE.EXPORTACAO_UVA.descricao,
    description="Consulta a Base de Exportação Uvas Frescas \
        e retorna os dados em formato JSON.",
)
async def exportacao_uva(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Exportação Uvas Frescas."""
    logger.debug("Chamada /exportacao_uva - funcao exportacao_uva")
    consulta = Consultar(BASE.EXPORTACAO_UVA)
    return consulta.executa()


@consulta.get(
    "/exportacao_suco",
    summary=BASE.EXPORTACAO_SUCO.descricao,
    description=(
        "Consulta a Base de Exportação Suco de uva \
            e retorna os dados em formato JSON."
    ),
)
async def exportacao_suco(
        user=Depends(AuthenticationService().get_token_header)) -> str:
    """Consulta da Base de Exportação Suco de uva."""
    logger.debug("Chamada /exportacao_suco - funcao exportacao_suco")
    consulta = Consultar(BASE.EXPORTACAO_SUCO)
    return consulta.executa()

"""API simples."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar, forma_descricao

importacao = APIRouter(prefix="/importacao",
                       tags=["Consulta a dados de Importação"])


logger = logging.getLogger("main.app.router.imortacao")


@importacao.get(
    "/vinhos",
    summary=BASE.IMPORTACAO_VINHOS.descricao,
    description=forma_descricao(BASE.IMPORTACAO_VINHOS),
    response_model=BASE.IMPORTACAO_VINHOS.response_model,
)
async def importacao_vinhos(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Importação Vinhos de Mesa."""
    logger.debug("Chamada /importacao_vinhos - funcao importacao_vinhos")
    consulta = Consultar(BASE.IMPORTACAO_VINHOS)
    return JSONResponse(consulta.executa())


@importacao.get(
    "/espumantes",
    summary=BASE.IMPORTACAO_ESPUMANTES.descricao,
    description=forma_descricao(BASE.IMPORTACAO_ESPUMANTES),
    response_model=BASE.IMPORTACAO_ESPUMANTES.response_model,
)
async def importacao_espumantes(
        user=Depends(AuthenticationService().get_token_header)

) -> JSONResponse:
    """Consulta da Base de Importação Espumantes."""
    logger.debug(
        "Chamada /importacao_espumantes - funcao importacao_espumantes")
    consulta = Consultar(BASE.IMPORTACAO_ESPUMANTES)
    return JSONResponse(consulta.executa())


@importacao.get(
    "/uvas",
    summary=BASE.IMPORTACAO_UVAS.descricao,
    description=forma_descricao(BASE.IMPORTACAO_UVAS),
    response_model=BASE.IMPORTACAO_UVAS.response_model,
)
async def importacao_uvas(
        user=Depends(AuthenticationService().get_token_header)

) -> JSONResponse:
    """Consulta da Base de Importação Uvas Frescas."""
    logger.debug("Chamada /importacao_uvas - funcao importacao_uvas")
    consulta = Consultar(BASE.IMPORTACAO_UVAS)
    return JSONResponse(consulta.executa())


@importacao.get(
    "/passas",
    summary=BASE.IMPORTACAO_PASSAS.descricao,
    description=forma_descricao(BASE.IMPORTACAO_PASSAS),
    response_model=BASE.IMPORTACAO_PASSAS.response_model,
)
async def importacao_passas(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Importação Uvas Passas."""
    logger.debug("Chamada /importacao_passas - funcao importacao_passas")
    consulta = Consultar(BASE.IMPORTACAO_PASSAS)
    return JSONResponse(consulta.executa())


@importacao.get(
    "/suco",
    summary=BASE.IMPORTACAO_SUCO.descricao,
    description=forma_descricao(BASE.IMPORTACAO_SUCO),
    response_model=BASE.IMPORTACAO_SUCO.response_model,
)
async def importacao_suco(
        user=Depends(AuthenticationService().get_token_header)

) -> JSONResponse:
    """Consulta da Base de Importação Suco de uva."""
    logger.debug("Chamada /importacao_suco - funcao importacao_suco")
    consulta = Consultar(BASE.IMPORTACAO_SUCO)
    return JSONResponse(consulta.executa())

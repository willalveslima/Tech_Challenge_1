"""API simples."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar, forma_descricao

processamento = APIRouter(prefix="/processamento",
                          tags=["Consulta Dados de Processamento"])


logger = logging.getLogger("main.app.router.processamento")


@processamento.get(
    "/viniferas",
    summary=BASE.PROCESSAMENTO_VINIFERAS.descricao,
    description=forma_descricao(BASE.PROCESSAMENTO_VINIFERAS),
    response_model=BASE.PROCESSAMENTO_VINIFERAS.response_model,
)
async def processamento_viniferas(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Processamento de Viníferas."""
    logger.debug(
        "Chamada /processamento_viniferas - funcao processamento_viniferas")
    consulta = Consultar(BASE.PROCESSAMENTO_VINIFERAS)
    return JSONResponse(consulta.executa())


@processamento.get(
    "/americanas",
    summary=BASE.PROCESSAMENTO_AMERICANAS.descricao,
    description=forma_descricao(BASE.PROCESSAMENTO_AMERICANAS),
    response_model=BASE.PROCESSAMENTO_AMERICANAS.response_model,
)
async def processamento_americanas(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Processamento Americanas."""
    logger.debug(
        "Chamada /processamento_americanas - funcao processamento_americanas")
    consulta = Consultar(BASE.PROCESSAMENTO_AMERICANAS)
    return JSONResponse(consulta.executa())


@processamento.get(
    "/mesa",
    summary=BASE.PROCESSAMENTO_MESA.descricao,
    description=forma_descricao(BASE.PROCESSAMENTO_MESA),
    response_model=BASE.PROCESSAMENTO_MESA.response_model,
)
async def processamento_mesa(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Processamento Uvas de Mesa."""
    logger.debug("Chamada /processamento_mesa - funcao processamento_mesa")
    consulta = Consultar(BASE.PROCESSAMENTO_MESA)
    return JSONResponse(consulta.executa())


@processamento.get(
    "/sem_classi",
    summary=BASE.PROCESSAMENTO_SEM_CLASSI.descricao,
    description=forma_descricao(BASE.PROCESSAMENTO_SEM_CLASSI),
    response_model=BASE.PROCESSAMENTO_SEM_CLASSI.response_model,
)
async def processamento_sem_classi(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Sem Classificação."""
    logger.debug(
        "Chamada /processamento_sem_classi - funcao processamento_sem_classi")
    consulta = Consultar(BASE.PROCESSAMENTO_SEM_CLASSI)
    return JSONResponse(consulta.executa())

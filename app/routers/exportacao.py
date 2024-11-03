"""API simples."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar, forma_descricao

exportacao = APIRouter(prefix="/exportacao",
                       tags=["Consulta dados de Exportação"])


logger = logging.getLogger("main.app.router.exportacao")


@exportacao.get(
    "/vinho",
    summary=BASE.EXPORTACAO_VINHO.descricao,
    description=forma_descricao(BASE.EXPORTACAO_VINHO),
    response_model=BASE.EXPORTACAO_VINHO.response_model,
)
async def exportacao_vinho(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Exportação Vinho de Mesa."""
    logger.debug("Chamada /exportacao_vinho - funcao exportacao_vinho")
    consulta = Consultar(BASE.EXPORTACAO_VINHO)
    return JSONResponse(consulta.executa())


@exportacao.get(
    "/espumante",
    summary=BASE.EXPORTACAO_ESPUMANTE.descricao,
    description=forma_descricao(BASE.EXPORTACAO_ESPUMANTE),
    response_model=BASE.EXPORTACAO_ESPUMANTE.response_model,
)
async def exportacao_espumante(
        user=Depends(AuthenticationService().get_token_header)

) -> JSONResponse:
    """Consulta da Base de Exportação Espumante."""
    logger.debug("Chamada /exportacao_espumante - funcao exportacao_espumante")
    consulta = Consultar(BASE.EXPORTACAO_ESPUMANTE)
    return JSONResponse(consulta.executa())


@exportacao.get(
    "/uva",
    summary=BASE.EXPORTACAO_UVA.descricao,
    description=forma_descricao(BASE.EXPORTACAO_UVA),
    response_model=BASE.EXPORTACAO_UVA.response_model,
)
async def exportacao_uva(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Exportação Uvas Frescas."""
    logger.debug("Chamada /exportacao_uva - funcao exportacao_uva")
    consulta = Consultar(BASE.EXPORTACAO_UVA)
    return JSONResponse(consulta.executa())


@exportacao.get(
    "/suco",
    summary=BASE.EXPORTACAO_SUCO.descricao,
    description=forma_descricao(BASE.EXPORTACAO_SUCO),
    response_model=BASE.EXPORTACAO_SUCO.response_model,
)
async def exportacao_suco(
        user=Depends(AuthenticationService().get_token_header)

) -> JSONResponse:
    """Consulta da Base de Exportação Suco de uva."""
    logger.debug("Chamada /exportacao_suco - funcao exportacao_suco")
    consulta = Consultar(BASE.EXPORTACAO_SUCO)
    return JSONResponse(consulta.executa())

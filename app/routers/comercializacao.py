"""API simples."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar, forma_descricao

comercializacao = APIRouter(tags=["Consulta a dados de Comercialização"])


logger = logging.getLogger("main.app.router.comercializacao")


@comercializacao.get(
    "/comercializacao",
    summary=BASE.COMERCIALIZACAO.descricao,
    description=forma_descricao(BASE.COMERCIALIZACAO),
    response_model=BASE.COMERCIALIZACAO.response_model,
)
async def get_comercializacao(
        user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Comercialização."""
    logger.debug("Chamada /comercializacao - funcao get_comercializacao")
    consulta = Consultar(BASE.COMERCIALIZACAO)
    return JSONResponse(consulta.executa())

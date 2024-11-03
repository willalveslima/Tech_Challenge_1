"""API simples."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.services.authentication import AuthenticationService
from app.services.consulta_bases import BASE, Consultar, forma_descricao

producao = APIRouter(tags=["Consulta Dados de Produção"])


logger = logging.getLogger("main.app.router.producao")


@producao.get(
    "/producao",
    summary=BASE.PRODUCAO.descricao,
    description=forma_descricao(BASE.PRODUCAO),
    response_model=BASE.PRODUCAO.response_model,
)
async def get_producao(
    user=Depends(AuthenticationService().get_token_header)
) -> JSONResponse:
    """Consulta da Base de Produção."""
    logger.debug("Chamada /producao - funcao get_producao")
    consulta = Consultar(BASE.PRODUCAO)
    return JSONResponse(consulta.executa())

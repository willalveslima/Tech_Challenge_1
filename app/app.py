"""API simples."""
from fastapi import FastAPI

from app.constants import BASE
from app.utils import consultar_base, erro_500
from app.model import Consultar,BASE2

app = FastAPI()


@app.get("/producao",  summary=BASE2.PRODUCAO.descricao,
         description="Consulta a Base de Produção de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def teste() -> str:
    """Consulta da Base de Produção, retorna os dados em formato JSON."""
    consulta = Consultar(BASE2.PRODUCAO)
    return consulta.executa()

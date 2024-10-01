"""API simples."""
from fastapi import FastAPI

from app.constants import BASE
from app.utils import consultar_base, erro_500
from app.model import Consultar,BASE2

app = FastAPI()


@app.get("/producao",  summary="Consulta a Base de Produção",
         description="Consulta a Base de Produção de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def consultar_producao() -> str:
    """Consulta da Base de Produção, retorna os dados em formato JSON."""
    try:
        return consultar_base(BASE.PRODUCAO)
    except Exception as e:
        erro_500(e, BASE.PRODUCAO)


@app.get("/comercializacao", summary="Consulta a Base de Comercialização",
         description="Consulta a Base de Comercialização de vinhos " +
         "da Empraba e retorna os dados em formato JSON.")
async def consultar_comercializacao() -> str:
    """consultar_comercializacao.

    Consulta da Base de Comercialização, retorna os dados em formato JSON.
    """
    try:
        return consultar_base(BASE.COMERCIALIZACAO)
    except Exception as e:
        erro_500(e, BASE.COMERCIALIZACAO)


@app.get("/exportacao", summary="Consulta a Base de Exportação",
         description="Consulta a Base de Exportação de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def consultar_exportacao() -> str:
    """Consulta da Base de Exportação, retorna os dados em formato JSON."""
    try:
        return consultar_base(BASE.EXPORTACAO)
    except Exception as e:
        erro_500(e, BASE.EXPORTACAO)


@app.get("/importacao", summary="Consulta a Base de Importação",
         description="Consulta a Base de Importação de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def consultar_importacao() -> str:
    """Consulta da Base de Importação, retorna os dados em formato JSON."""
    try:
        return consultar_base(BASE.IMPORTACAO)
    except Exception as e:
        erro_500(e, BASE.IMPORTACAO)


@app.get("/processamento", summary="Consulta a Base de Processamento",
         description="Consulta a Base de Processamento de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def consultar_processamento() -> str:
    """Consulta da Base de Processamento, retorna os dados em formato JSON."""
    try:
        return consultar_base(BASE.PROCESSAMENTO)
    except Exception as e:
        erro_500(e, BASE.PROCESSAMENTO)


@app.get("/teste",  summary="Consulta a Base de Produção",
         description="Consulta a Base de Produção de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def teste() -> str:
    """Consulta da Base de Produção, retorna os dados em formato JSON."""
    try:
        consulta = Consultar(BASE2.PRODUCAO)
        return consulta.executa()
    except Exception as e:
        erro_500(e, BASE.PRODUCAO)

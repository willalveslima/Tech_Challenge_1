"""API simples."""
from fastapi import FastAPI
from app.model import Consultar, BASE

app = FastAPI()


@app.get("/producao",  summary=BASE.PRODUCAO.descricao,
         description="Consulta a Base de Produção de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def teste() -> str:
    """Consulta da Base de Produção, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.PRODUCAO)
    return consulta.executa()


@app.get("/processamento_viniferas", summary=BASE.PROCESSAMENTO_VINIFERAS.descricao,
         description="Consulta a Base de Processamento Viniferas e retorna os dados em formato JSON.")
async def processamento_viniferas() -> str:
    """Consulta da Base de Processamento Viniferas, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.PROCESSAMENTO_VINIFERAS)
    return consulta.executa()


@app.get("/processamento_americanas", summary=BASE.PROCESSAMENTO_AMERICANAS.descricao,
         description="Consulta a Base de Processamento Americanas e retorna os dados em formato JSON.")
async def processamento_americanas() -> str:
    """Consulta da Base de Processamento Americanas, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.PROCESSAMENTO_AMERICANAS)
    return consulta.executa()


@app.get("/processamento_mesa", summary=BASE.PROCESSAMENTO_MESA.descricao,
         description="Consulta a Base de Processamento Uvas de Mesa e retorna os dados em formato JSON.")
async def processamento_mesa() -> str:
    """Consulta da Base de Processamento Uvas de Mesa, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.PROCESSAMENTO_MESA)
    return consulta.executa()


@app.get("/processamento_sem_classi", summary=BASE.PROCESSAMENTO_SEM_CLASSI.descricao,
         description="Consulta a Base de Sem Classificação e retorna os dados em formato JSON.")
async def processamento_sem_classi() -> str:
    """Consulta da Base de Sem Classificação, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.PROCESSAMENTO_SEM_CLASSI)
    return consulta.executa()


@app.get("/comercializacao", summary=BASE.COMERCIALIZACAO.descricao,
         description="Consulta a Base de Comercialização e retorna os dados em formato JSON.")
async def comercializacao() -> str:
    """Consulta da Base de Comercialização, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.COMERCIALIZACAO)
    return consulta.executa()


@app.get("/importacao_vinhos", summary=BASE.IMPORTACAO_VINHOS.descricao,
         description="Consulta a Base de Importação Vinhos de Mesa e retorna os dados em formato JSON.")
async def importacao_vinhos() -> str:
    """Consulta da Base de Importação Vinhos de Mesa, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.IMPORTACAO_VINHOS)
    return consulta.executa()


@app.get("/importacao_espumantes", summary=BASE.IMPORTACAO_ESPUMANTES.descricao,
         description="Consulta a Base de Importação Espumantes e retorna os dados em formato JSON.")
async def importacao_espumantes() -> str:
    """Consulta da Base de Importação Espumantes, retorna os dados em formato JSON."""
    consulta = Consultar(BASE.IMPORTACAO_ESPUMANTES)
    return consulta.executa()


@app.get("/importacao_uvas", summary=BASE.IMPORTACAO_UVAS.descricao,
         description="Consulta a Base de Importação Uvas Frescas e retorna os dados em formato JSON.")
async def importacao_uvas() -> str:
    consulta = Consultar(BASE.IMPORTACAO_UVAS)
    return consulta.executa()


@app.get("/importacao_passas", summary=BASE.IMPORTACAO_PASSAS.descricao,
         description="Consulta a Base de Importação Uvas Passas e retorna os dados em formato JSON.")
async def importacao_passas() -> str:
    consulta = Consultar(BASE.IMPORTACAO_PASSAS)
    return consulta.executa()


@app.get("/importacao_suco", summary=BASE.IMPORTACAO_SUCO.descricao,
         description="Consulta a Base de Importação Suco de uva e retorna os dados em formato JSON.")
async def importacao_suco() -> str:
    consulta = Consultar(BASE.IMPORTACAO_SUCO)
    return consulta.executa()


@app.get("/exportacao_vinho", summary=BASE.EXPORTACAO_VINHO.descricao,
         description="Consulta a Base de Exportação Vinho de Mesa e retorna os dados em formato JSON.")
async def exportacao_vinho() -> str:
    consulta = Consultar(BASE.EXPORTACAO_VINHO)
    return consulta.executa()


@app.get("/exportacao_espumante", summary=BASE.EXPORTACAO_ESPUMANTE.descricao,
         description="Consulta a Base de Exportação Espumante e retorna os dados em formato JSON.")
async def exportacao_espumante() -> str:
    consulta = Consultar(BASE.EXPORTACAO_ESPUMANTE)
    return consulta.executa()


@app.get("/exportacao_uva", summary=BASE.EXPORTACAO_UVA.descricao,
         description="Consulta a Base de Exportação Uvas Frescas e retorna os dados em formato JSON.")
async def exportacao_uva() -> str:
    consulta = Consultar(BASE.EXPORTACAO_UVA)
    return consulta.executa()


@app.get("/exportacao_suco", summary=BASE.EXPORTACAO_SUCO.descricao,
         description="Consulta a Base de Exportação Suco de uva e retorna os dados em formato JSON.")
async def exportacao_suco() -> str:
    consulta = Consultar(BASE.EXPORTACAO_SUCO)
    return consulta.executa()

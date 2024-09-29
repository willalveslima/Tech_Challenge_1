"""API simples."""
from fastapi import FastAPI, HTTPException, status

from app.constants import (URL_BASE_COMERCIALIZACAO, URL_BASE_EXPORTACAO,
                           URL_BASE_IMPORTACAO, URL_BASE_PROCESSAMENTO,
                           URL_BASE_PRODUCAO)
from app.utils import convertar_para_json, ler_base_dados_csv

app = FastAPI()


@app.get("/producao",  summary="Consulta a Base de Produção",
         description="Consulta a Base de Produção de vinhos da Empraba " +
         "e retorna os dados em formato JSON.")
async def consultar_producao() -> str:
    """Consulta da Base de Produção, retorna os dados em formato JSON."""
    try:
        df_producao = ler_base_dados_csv(URL_BASE_PRODUCAO)
        return convertar_para_json(df_producao)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao ao consultar a base de Produção: {str(e)}",
        )


@app.get("/processamento", summary="Consulta a Base de Processamento",
         description=("Consulta a Base de Processamento de vinhos da Empraba "
                      "e retorna os dados em formato JSON."))
async def consultar_processamento() -> str:
    """Consulta da Base de Processamento, retorna os dados em formato JSON."""
    try:
        df_processamento = ler_base_dados_csv(URL_BASE_PROCESSAMENTO)
        return convertar_para_json(df_processamento)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao ao consultar a base de Processamento: {str(e)}",
        )


@app.get("/comercializacao", summary="Consulta a Base de Comercialização",
         description="Consulta a Base de Comercialização de vinhos da Empraba"
         "e retorna os dados em formato JSON.")
async def consultar_comercializacao() -> str:
    """consultar_comercializacao.

    Consulta da Base de Comercialização,
    retorna os dados em formato JSON.
    """
    try:
        df_comercializacao = ler_base_dados_csv(URL_BASE_COMERCIALIZACAO)
        return convertar_para_json(df_comercializacao)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao ao consultar a base de Comercialização: {str(e)}",
        )


@app.get("/importacao", summary="Consulta a Base de Importação",
         description="Consulta a Base de Importação de vinhos da Empraba"
         " e retorna os dados em formato JSON.")
async def consultar_importacao() -> str:
    """Consulta da Base de Importação, retorna os dados em formato JSON."""
    try:
        df_importacao = ler_base_dados_csv(URL_BASE_IMPORTACAO)
        return convertar_para_json(df_importacao)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao ao consultar a base de Importação: {str(e)}",
        )


@app.get("/exportacao", summary="Consulta a Base de Exportação",
         description="Consulta a Base de Exportação de vinhos da Empraba"
         " e retorna os dados em formato JSON.")
async def consultar_exportacao() -> str:
    """Consulta da Base de Exportação, retorna os dados em formato JSON."""
    try:
        df_exportacao = ler_base_dados_csv(URL_BASE_EXPORTACAO)
        return convertar_para_json(df_exportacao)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao ao consultar a base de Exportação: {str(e)}",
        )

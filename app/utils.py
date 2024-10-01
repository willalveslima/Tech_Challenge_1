"""Funçoes auxiliares."""
import pandas as pd
from fastapi import HTTPException

from app.constants import BASE


def ler_base_dados_csv(url_base_dados_csv: str) -> pd.DataFrame:
    """ler_base_dados.

    ler_base_dados_csv Realiza leitura de um arquivo CSV
    em uma URL e retorna um DataFrame.
    """
    return pd.read_csv(url_base_dados_csv, sep=";")


def converter_para_json(df: pd.DataFrame) -> str:
    """converter_para_json Converte um DataFrame em um JSON."""
    return df.to_json(orient="records")


def consultar_base(base: BASE) -> str:
    """Consulta a base de dados."""
    return converter_para_json(ler_base_dados_csv(base.url))


def erro_500(e: Exception, base: BASE) -> HTTPException:
    """erro_consultar_base."""
    raise HTTPException(
        status_code=500,
        detail=f"Erro ao ao consultar a {base.descricao}: {str(e)}",
    )

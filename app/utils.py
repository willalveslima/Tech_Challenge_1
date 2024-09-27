"""funçoes auxiliares"""
import pandas as pd

def ler_base_dados_csv(url_base_dados_csv: str) -> pd.DataFrame:
    """
    ler_base_dados_csv Realiza leitura de um arquivo CSV em uma URL e retorna um DataFrame.

    Args:
        url_base_dados_csv (str): URL do arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados do arquivo CSV.
    """
    return pd.read_csv(url_base_dados_csv)

def convertar_para_json(df: pd.DataFrame) -> str:
    """
    convertar_para_json Converte um DataFrame em um JSON.

    Args:
        df (pd.DataFrame): DataFrame a ser convertido.

    Returns:
        str: JSON gerado a partir do DataFrame.
    """
    return df.to_json(orient="records")


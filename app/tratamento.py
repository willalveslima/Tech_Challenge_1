"""Tratamento dos colonas recebidas do arquivo CSV."""

import logging

import pandas as pd

logger = logging.getLogger("main.app.tratamento")


class TratamentoColunaAnoSimples:
    """tranforma tabela no formato wide em long (ANO e QTD)."""

    def tratar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Trata as colunas do DataFrame."""
        logger.debug(
            "TratamentoColunaAnoSimples().tratar(): " +
            "Tratando colunas do DataFrame..."
        )
        # Excluir a coluna 'id'
        df = df.drop(columns=["id"])

        # Substituir os valores do campo 'control'
        df["control"] = df["control"].replace(
            {
                r"^vm_.*$": "VINHO DE MESA",
                r"^vv_.*$": "VINHO FINO DE MESA (VINIFERA)",
                r"^su_.*$": "SUCO",
                r"^de_.*$": "DERIVADOS",
                r"^es_.*$": "ESPUMANTE",
                r"^vi_.*$": "VINHO FINO",
                r"^ve_.*$": "VINHO ESPECIAIS",
                r"^ti_.*$": "TINTAS",
                r"^br_.*$": (
                    "BRANCAS E ROSADAS"
                    if "BRANCAS E ROSADAS" in df["control"].values
                    else "BRANCAS"
                ),
                r"^ou_.*$": "OUTROS",
                r"^co_.*$": "CONCENTRADO",
                r"^pa_.*$": "PASSAS",
                r"^fr_.*$": "FRESCAS",
                r"^se_.*$": "SEMENTES",
                r"^sc_.*$": "SEM CLASSIFICAÇÃO",
            },
            regex=True,
        )

        # Identificar as colunas a serem mantidas
        id_vars = ""
        value_name = "Kg"

        if "produto" in df.columns:
            df["produto"] = df["produto"].str.upper()
            id_vars = ["control", "produto"]
            value_name = "L"
        if "Produto" in df.columns:
            df["Produto"] = df["Produto"].str.upper()
            id_vars = ["control", "Produto"]
            value_name = "L"
        if "cultivar" in df.columns:
            df["cultivar"] = df["cultivar"].str.upper()
            id_vars = ["control", "cultivar"]

        # Identificar as colunas a serem derretidas (da 3ª até a última)
        value_vars = df.columns[2:]

        # Transformar as colunas a partir da 3ª até a última em valores
        df = df.melt(
            id_vars=id_vars,
            value_vars=value_vars,
            var_name="ANO",
            value_name=value_name,
        )

        # Renomear as colunas 'control' para 'Tipo' e 'produto' para 'PRODUTO'
        df = df.rename(
            columns={
                "control": "CONTROL",
                "produto": "PRODUTO",
                "Produto": "PRODUTO",
                "cultivar": "CULTIVAR",
            }
        )
        logger.debug("Colunas tratadas com sucesso.")
        return df


class TratamentoColunaAnoDuplo:
    """tranforma tabela no formato wide em long (ANO e KG e US$)."""

    def tratar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Trata as colunas do DataFrame."""
        logger.debug(
            "TratamentoColunaAnoDuplo().tratar(): \
                Tratando colunas do DataFrame..."
        )
        # Separar as colunas que terminam com .1 para df2 e as demais para df1
        df1 = df[[col for col in df.columns if not col.endswith(".1")]]
        df2 = df[["Id", "País"] +
                 [col for col in df.columns if col.endswith(".1")]]

        # Renomear as colunas de df2 para remover o sufixo .1
        df2.columns = [
            col.replace(".1", "") if col not in ["Id", "País"] else col
            for col in df2.columns
        ]
        value_vars = df1.columns[2:]
        # Realizar o melt em df1
        df1_melted = df1.melt(
            id_vars=["Id", "País"],
            value_vars=value_vars,
            var_name="Ano",
            value_name="KG",
        )

        value_vars = df2.columns[2:]
        # Realizar o melt em df2
        df2_melted = df2.melt(
            id_vars=["Id", "País"],
            value_vars=value_vars,
            var_name="Ano",
            value_name="US$",
        )

        # Fazer o merge entre df1_melted e df2_melted
        merged_df = pd.merge(df1_melted, df2_melted, on=["Id", "País", "Ano"])

        df = merged_df.drop(columns=["Id"])
        logger.debug("Colunas tratadas com sucesso.")
        return df

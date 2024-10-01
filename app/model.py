import pandas as pd
from enum import Enum

URL_BASE_PRODUCAO = "http://127.0.0.1/Producao.csv"

class TratamentoProducao():
    def tratar(self, df: pd.DataFrame) -> pd.DataFrame:
        # Excluir a coluna 'id'
        df = df.drop(columns=['id'])

        # Excluir as linhas onde o campo 'control' é igual ao campo 'produto'
        df = df[df['control'] != df['produto']]
        
        # Substituir os valores do campo 'control' conforme a tabela fornecida
        df['control'] = df['control'].replace({
            r'^vm_.*$': 'VINHO DE MESA',
            r'^vv_.*$': 'VINHO FINO DE MESA (VINIFERA)',
            r'^su_.*$': 'SUCO',
            r'^de_.*$': 'DERIVADOS'   
        }, regex=True)

        # Mudar os valores do campo 'produto' para maiúsculas
        df['produto'] = df['produto'].str.upper()

        # Identificar as colunas a serem mantidas
        id_vars = ['control', 'produto']

        # Identificar as colunas a serem derretidas (da 3ª até a última)
        value_vars = df.columns[2:]

        # Transformar as colunas a partir da 3ª até a última em valores
        df = df.melt(id_vars=id_vars, value_vars=value_vars, var_name='ANO', value_name='LITROS')

        # Renomear as colunas 'control' para 'Tipo' e 'produto' para 'PRODUTO'
        df = df.rename(columns={'control': 'Tipo', 'produto': 'PRODUTO'})
       
        return df


class BASE2(Enum):
    """Enum com as bases de dados."""

    PRODUCAO = (URL_BASE_PRODUCAO, "Base de Produção", TratamentoProducao())
    PROCESSAMENTO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "Base de Processamento",None)
    COMERCIALIZACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "Base de Comercialização",None)
    IMPORTACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "Base de Importação",None)
    EXPORTACAO = (
        "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "Base de Exportação", None)

    def __init__(self, url, descricao, tratamento):
        """Construtor."""
        self.url = url
        self.descricao = descricao
        self.tratamento = tratamento


class Consultar():
    def __init__(self, base: BASE2):
        self.base = base
        self.df = None
    def executa(self):
      
        self.df = pd.read_csv(self.base.url, sep=";")
        if self.base.tratamento is not None:
            self.df = self.base.tratamento.tratar(self.df)
        return self.df.to_json(orient="records")    


        
    


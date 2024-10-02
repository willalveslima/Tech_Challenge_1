import pandas as pd
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
        df = df.rename(columns={'control': 'TIPO', 'produto': 'PRODUTO'})
       
        return df

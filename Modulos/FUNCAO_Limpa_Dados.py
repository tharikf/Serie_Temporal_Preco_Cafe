
'''
Essa função realiza a limpeza dos dados brutos retirados do site da ESALQ.
'''

import pandas as pd

import warnings
warnings.filterwarnings("ignore")

def limpando_dados(df):
    
    # Alterando nomes das colunas:
    df.columns = ['data', 'preco_reais', 'preco_dolar']
    
    # Dropando coluna dolar
    df = df[['data', 'preco_reais']]
    
    # Trocando virgula por ponto e transformando em float
    for col in list(df.columns)[1:]:
        df[col] = df[col].apply(lambda x: x.replace(',', '.')).astype(float)

    
    # Transformando em data
    df['data'] = pd.to_datetime(df['data'], format = '%d/%m/%Y')
    
    # Colocando a data como indice
    df.set_index("data", inplace = True)
        
    return df






'''
Função que aplica correção de valores de uma série temporal pela inflação.
'''

import pandas as pd
import numpy as np

def corrigindo_inflacao(df_treino, df_inflacao):
    
    # Alterando df_treino
    df_treino = df_treino.reset_index()
    df_treino['ano_mes'] = df_treino['data'].dt.to_period('M')
    
    # Unindo os dois dataframes
    df_pronto = pd.merge(df_treino, df_inflacao, left_on = 'ano_mes', right_on = 'Data', how = 'inner')
    
    # Colocando a data no indice
    df_pronto.set_index('data', inplace = True)
    
    # Deflacionando para preços de 2019
    df_pronto['indice_2019'] = 1 * (1 + df_pronto['Taxa_Diaria'])
    df_pronto.tail(1).iloc[0,-1] = 1
    df_pronto['inflacao_acumulada'] = np.flipud(np.flipud(df_pronto['indice_2019']).cumprod())
    
    # Corrigido pela inflação
    df_pronto['preco_corrigido'] = round(df_pronto['preco_reais'] / df_pronto['inflacao_acumulada'], 2)
    
    # Mantendo colunas relevantes
    df_pronto = df_pronto[['preco_reais', 'preco_corrigido']]
    
    return df_pronto





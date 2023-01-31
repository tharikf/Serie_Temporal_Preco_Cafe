
'''
Essa função realiza o cálculo para médias móveis de uma série temporal.
'''

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error


def calculo_media_movel(dataframe, coluna, dias):
    
    # Media movel
    df_copia = dataframe.copy()
    df_copia['media_movel'] = round(df_copia[coluna].rolling(window = dias).mean(), 2)
    
    # Retirando valores NA
    df_copia = df_copia.dropna()
    
    # Criando intervalo de confiança (95% de confiança - 1.96)
    erro_medio = mean_absolute_error(df_copia['preco_reais'], df_copia['media_movel'])
    desvio_padrao = np.std(df_copia['preco_reais'] - df_copia['media_movel'])
    df_copia['mm_limite_abaixo'] = round(df_copia['media_movel'] - (erro_medio + (1.96 * desvio_padrao)), 2)
    df_copia['mm_limite_acima'] = round(df_copia['media_movel'] + (erro_medio + (1.96 * desvio_padrao)), 2)
    
    
    return df_copia


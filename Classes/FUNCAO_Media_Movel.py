
'''
Essa função realiza o cálculo para médias móveis de uma série temporal.
'''

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error


def calculo_media_movel(dataframe, coluna, dias):
    
    # Media movel
    dataframe['media_movel'] = round(dataframe[coluna].rolling(window = dias).mean(), 2)
    
    # Retirando valores NA
    dataframe = dataframe.dropna()
    
    # Criando intervalo de confiança (95% de confiança - 1.96)
    erro_medio = mean_absolute_error(dataframe['preco_reais'], dataframe['media_movel'])
    desvio_padrao = np.std(dataframe['preco_reais'] - dataframe['media_movel'])
    dataframe['mm_limite_abaixo'] = round(dataframe['media_movel'] - (erro_medio + (1.96 * desvio_padrao)), 2)
    dataframe['mm_limite_acima'] = round(dataframe['media_movel'] + (erro_medio + (1.96 * desvio_padrao)), 2)
    
    
    return dataframe


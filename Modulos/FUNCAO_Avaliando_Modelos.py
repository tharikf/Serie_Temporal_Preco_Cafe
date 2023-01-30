
'''
Função que cria métodos de avaliação dos modelos de previsão que serão testados.
'''

import pandas as pd
import numpy as np
from math import sqrt
from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error, mean_squared_error, mean_squared_error


def AvaliandoModelos(valores_teste, valores_previstos, nome_col = '', nome_indice = ''):

    # Erro Quadrado Médio
    mse = mean_squared_error(valores_teste, valores_previstos)

    # Raiz do Erro Quadrado Médio
    rmse = sqrt(mean_squared_error(valores_teste, valores_previstos))

    # Erro Absoluto Médio
    mae = mean_absolute_error(valores_teste, valores_previstos)

    # Erro Absoluto Médio em Percentual
    mape = np.mean(np.abs((valores_teste - valores_previstos) / valores_teste)) * 100

    # Colocando em um DataFrame
    metricas = [mse, rmse, mae, mape]

    metricas_df = pd.DataFrame(metricas, index = ['MSE', 'RMSE', 'MAE', 'MAPE'], columns = [nome_col])
    metricas_df.index.name = nome_indice

    return metricas_df




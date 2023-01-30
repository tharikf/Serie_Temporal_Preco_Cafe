
'''
Classe que cria métodos de avaliação dos modelos de previsão que serão testados.
'''

import pandas as pd
import numpy as np
from math import sqrt
from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error, mean_squared_error, mean_squared_error


class AvaliandoModelos:

    def __init__(self, valores_teste, valores_previstos, nome_col = '', nome_indice = ''):

        self.valores_teste = valores_teste
        self.valores_previstos = valores_previstos
        self.nome_col = nome_col
        self.nome_indice = nome_indice

        self.metricas_df = None


    def metricas_avaliacao(self):

        # Erro Quadrado Médio
        mse = mean_squared_error(self.valores_teste, self.valores_previstos)

        # Raiz do Erro Quadrado Médio
        rmse = sqrt(mean_squared_error(self.valores_teste, self.valores_previstos))

        # Erro Absoluto Médio
        mae = mean_absolute_error(self.valores_teste, self.valores_previstos)

        # Erro Absoluto Médio em Percentual
        mape = np.mean(np.abs((self.valores_teste - self.valores_previstos) / self.valores_teste)) * 100

        # Colocando em um DataFrame
        metricas = [mse, rmse, mae, mape]

        self.metricas_df = pd.DataFrame(metricas, index = ['MSE', 'RMSE', 'MAE', 'MAPE'], columns = [self.nome_col])
        self.metricas_df.index.name = self.nome_indice

        return self.metricas_df




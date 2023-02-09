
'''
Essa classe tem como objetivo reunir e plotar informações dos resíduos da previsão.
'''

import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

class PlotResiduos:

    def __init__(self, dataframe):
        self.dataframe = dataframe


    def plot_residuos(self):

        # Calculando Residuo
        self.dataframe['Residuos'] = self.dataframe.iloc[:, 0] - self.dataframe.iloc[:, 1]

        fig, [(ax1, ax2), (ax3, ax4)] = plt.subplots(2, 2, figsize = (12, 10))
        
        # Scatterplot Valores Reais e Residuos
        ax1.scatter(self.dataframe.iloc[:, 0], self.dataframe['Residuos'])
        ax1.set_xlabel('Valores Reais')
        ax1.set_ylabel('Residuos')

        # QQ Plot dos Residuos
        sm.graphics.qqplot(self.dataframe['Residuos'], line = 'r', ax = ax2)

        # ACF dos resíduos
        plot_acf(self.dataframe['Residuos'], lags = 10, ax = ax3)

        # PACF dos resíduos
        plot_pacf(self.dataframe['Residuos'], lags = 10, ax = ax4)

        return plt.show()







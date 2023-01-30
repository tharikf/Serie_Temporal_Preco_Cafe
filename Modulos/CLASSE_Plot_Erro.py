
'''
Essa classe tem como objetivo reunir e plotar informações dos resíduos da previsão.
'''

import matplotlib.pyplot as plt
import statsmodels.api as sm

class PlotResiduos:

    def __init__(self, dataframe):
        self.dataframe = dataframe


    def plot_residuos(self):

        # Calculando Residuo
        self.dataframe['Residuos'] = self.dataframe.iloc[:, 0] - self.dataframe.iloc[:, 1]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (8, 6))
        
        # Scatterplot Valores Reais e Residuos
        ax1.scatter(self.dataframe.iloc[:, 0], self.dataframe['Residuos'])
        ax1.set_xlabel('Valores Reais')
        ax1.set_ylabel('Residuos')

        # QQ Plot dos Residuos
        sm.graphics.qqplot(self.dataframe['Residuos'], line = 'r', ax = ax2)

        return plt.show()







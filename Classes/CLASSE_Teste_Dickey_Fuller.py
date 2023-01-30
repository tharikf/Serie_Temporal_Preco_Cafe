
'''
Essa classe realiza o teste de Dickey-Fuller e apresenta os resultados.
'''

from statsmodels.tsa.stattools import adfuller

class DickeyFuller:

    def __init__(self, dataframe):
        
        self.dataframe = dataframe
        self.valor_teste = None
        self.p_valor = None
        self.lags = None
        self.observacoes = None
        self.teste_dickey_fuller()

    def teste_dickey_fuller(self):

        # Realizando o teste
        self.resultado_DF = adfuller(self.dataframe)

        # Obtendo medidas de avaliacao do teste
        self.valor_teste = round(self.resultado_DF[0], 4)
        self.p_valor = round(self.resultado_DF[1], 4)
        self.lags = self.resultado_DF[2]
        self.observacoes = self.resultado_DF[3]


    def resultados_teste(self):

        print('Resultados do teste de Dickey-Fuller!')
        print('-' * 70)

        medidas = ['Valor Dickey-Fuller', 'p-valor', 'Lags', 'Observações']

        for i, j in zip(medidas, self.resultado_DF[0:4]):
            print(f'{i}: {round(j, 4)}')

        print('-' * 70)
        # Obtendo valores criticos
        for valor in self.resultado_DF[4].items():
            print(f'O valor crítico para um nível de significância de {valor[0]} é: {round(valor[1], 4)}')
        
        # Falha ou rejeita em falhar a hipótese nula
        if self.resultado_DF[1] >= 0.05:
            return 'Falhamos em rejeitar a hipótese nula! Sem evidência de estacionariedade!'
        else:
            return 'Rejeitamos a hipótese nula! Evidência de estacionariedade!'

        
    
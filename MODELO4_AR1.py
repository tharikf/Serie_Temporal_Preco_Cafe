
'''
Modelo 4 - Modelo AR1.
Treino e Teste do quarto modelo.
'''

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from Tratamento_Dados import treino, treino_diferenciado, teste, teste_diferenciado
from Modulos.FUNCAO_Avaliando_Modelos import AvaliandoModelos
from Modulos.FUNCAO_Retomando_Valores_Previsao import retomando_valor_previsto
from Modulos.CLASSE_Plot_Erro import PlotResiduos
from MODELO3_Media_Movel_Exponencial import avaliacao_treino, avaliacao_teste


                    # Avaliando em Treino #
modeloV4_AR1_treino = treino_diferenciado[['preco_reais']]
modeloV4_AR1_treino.columns = ['Observado']

modelo_v4 = ARIMA(modeloV4_AR1_treino['Observado'], order = [1, 0, 0]).fit()
modeloV4_AR1_treino['Previsto'] = modelo_v4.predict(start = 0, end = len(modeloV4_AR1_treino) - 1)

modeloV4_avalia_treino = retomando_valor_previsto(treino['preco_reais'], modeloV4_AR1_treino['Previsto'])

avaliacao_treino['ModeloV4_AR1'] = AvaliandoModelos(modeloV4_avalia_treino['Preco_Original'],
                                                    modeloV4_avalia_treino['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_treino)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV4_avalia_treino['Preco_Original'])
    plt.plot(modeloV4_avalia_treino['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV4_treino = PlotResiduos(modeloV4_avalia_treino)
    residuosV4_treino.plot_residuos()

if __name__ == '__main__':
    modelo_v4.summary()

                    # Avaliando em Teste #
modeloV4_AR1_teste = teste_diferenciado[['preco_reais']]
modeloV4_AR1_teste.columns = ['Observado']

coef_ar1 = modelo_v4.arparams.item()
hist = [modeloV4_AR1_treino.iloc[i, 0] for i in range(len(modeloV4_AR1_treino))]
lista_previsao = []

for t in range(len(modeloV4_AR1_teste)):
    yhat = (hist[-1] * coef_ar1)
    obs = modeloV4_AR1_teste.iloc[t, 0]
    lista_previsao.append(yhat)
    hist.append(obs)

modeloV4_AR1_teste['Previsto'] = lista_previsao

modeloV4_avalia_teste = retomando_valor_previsto(teste['preco_reais'], modeloV4_AR1_teste['Previsto'])

avaliacao_teste['ModeloV4_AR1'] = AvaliandoModelos(modeloV4_avalia_teste['Preco_Original'],
                                                   modeloV4_avalia_teste['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_teste)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV4_avalia_teste['Preco_Original'])
    plt.plot(modeloV4_avalia_teste['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV4_teste = PlotResiduos(modeloV4_avalia_teste)
    residuosV4_teste.plot_residuos()


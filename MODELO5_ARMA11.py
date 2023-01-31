
'''
Modelo 5 - Modelo ARMA (1, 1).
Treino e Teste do quinto modelo.
'''

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from Tratamento_Dados import treino, treino_diferenciado, teste, teste_diferenciado
from Modulos.FUNCAO_Avaliando_Modelos import AvaliandoModelos
from Modulos.FUNCAO_Retomando_Valores_Previsao import retomando_valor_previsto
from Modulos.CLASSE_Plot_Erro import PlotResiduos
from MODELO4_AR1 import avaliacao_treino, avaliacao_teste


                    # Avaliando em Treino #
modeloV5_ARMA_treino = treino_diferenciado[['preco_reais']]
modeloV5_ARMA_treino.columns = ['Observado']

modelo_v5 = ARIMA(modeloV5_ARMA_treino['Observado'], order = (1, 0, 1)).fit()
modeloV5_ARMA_treino['Previsto'] = modelo_v5.predict(start = 0, end = len(modeloV5_ARMA_treino) - 1)

modeloV5_avalia_treino = retomando_valor_previsto(treino['preco_reais'], modeloV5_ARMA_treino['Previsto'])

avaliacao_treino['ModeloV5_ARMA11'] = AvaliandoModelos(modeloV5_avalia_treino['Preco_Original'],
                                                    modeloV5_avalia_treino['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_treino)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV5_avalia_treino['Preco_Original'])
    plt.plot(modeloV5_avalia_treino['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV5_treino = PlotResiduos(modeloV5_avalia_treino)
    residuosV5_treino.plot_residuos()

if __name__ == '__main__':
    modelo_v5.summary()


                    # Avaliando em Teste #
modeloV5_ARMA_teste = teste_diferenciado[['preco_reais']]
modeloV5_ARMA_teste.columns = ['Observado']

coef_ar1 = modelo_v5.arparams.item()
coer_ma1 = modelo_v5.maparams.item()

hist = [modeloV5_ARMA_treino.iloc[i, 0] for i in range(len(modeloV5_ARMA_treino))]
error = [0.0 for i in range(len(modeloV5_ARMA_treino))]

lista_previsao = []

for t in range(len(modeloV5_ARMA_teste)):
    yhat = ((hist[-1] * coef_ar1) + (error[-1] * coer_ma1))
    obs = modeloV5_ARMA_teste.iloc[t, 0]
    lista_previsao.append(yhat)
    hist.append(obs)
    error.append(obs - yhat)

modeloV5_ARMA_teste['Previsto'] = lista_previsao

modeloV5_avalia_teste = retomando_valor_previsto(teste['preco_reais'], modeloV5_ARMA_teste['Previsto'])

avaliacao_teste['ModeloV5_ARMA11'] = AvaliandoModelos(modeloV5_avalia_teste['Preco_Original'],
                                                      modeloV5_avalia_teste['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_teste)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV5_avalia_teste['Preco_Original'])
    plt.plot(modeloV5_avalia_teste['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV5_teste = PlotResiduos(modeloV5_avalia_teste)
    residuosV5_teste.plot_residuos()

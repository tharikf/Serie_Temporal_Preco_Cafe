
'''
Modelo 3 - Média Móvel Exponencial.
Treino e Teste do terceiro modelo.
'''

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from Tratamento_Dados import treino, treino_diferenciado, teste, teste_diferenciado
from Modulos.FUNCAO_Avaliando_Modelos import AvaliandoModelos
from Modulos.FUNCAO_Retomando_Valores_Previsao import retomando_valor_previsto
from Modulos.CLASSE_Plot_Erro import PlotResiduos
from MODELO2_Media_Movel_5Dias import avaliacao_treino, avaliacao_teste


                    # Avaliando em Treino #
modeloV3_MME_treino = treino_diferenciado[['preco_reais']]
modeloV3_MME_treino.columns = ['Observado']

alpha = 0.5
modelo_v3 = ExponentialSmoothing(modeloV3_MME_treino['Observado']).fit(smoothing_level = alpha)
modeloV3_MME_treino['Previsto'] = modelo_v3.predict(start = 0, end = len(modeloV3_MME_treino) - 1)

modeloV3_avalia_treino = retomando_valor_previsto(treino['preco_reais'], modeloV3_MME_treino['Previsto'])

avaliacao_treino['ModeloV3_MME'] = AvaliandoModelos(modeloV3_avalia_treino['Preco_Original'],
                                                    modeloV3_avalia_treino['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_treino)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV3_avalia_treino['Preco_Original'])
    plt.plot(modeloV3_avalia_treino['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV3_treino = PlotResiduos(modeloV3_avalia_treino)
    residuosV3_treino.plot_residuos()

if __name__ == '__main__':
    print(modelo_v3.summary())


                    # Avaliando em Teste #
modeloV3_MME_teste = teste_diferenciado[['preco_reais']]
modeloV3_MME_teste.columns = ['Observado']

hist = [modeloV3_MME_treino.iloc[i, 0] for i in range(len(modeloV3_MME_treino))]
hist_prev = [modeloV3_MME_treino.iloc[i, 1] for i in range(len(modeloV3_MME_treino))]
lista_previsao = []

for t in range(len(modeloV3_MME_teste)):
    yhat = hist_prev[-1] + (alpha * (hist[-1] - hist_prev[-1]))
    obs = modeloV3_MME_teste.iloc[t, 0]
    lista_previsao.append(yhat)
    hist.append(obs)
    hist_prev.append(yhat)

modeloV3_MME_teste['Previsto'] = lista_previsao

modeloV3_avalia_teste = retomando_valor_previsto(teste['preco_reais'], modeloV3_MME_teste['Previsto'])

avaliacao_teste['ModeloV3_MME'] = AvaliandoModelos(modeloV3_avalia_teste['Preco_Original'],
                                                        modeloV3_avalia_teste['Preco_Previsto'])

if __name__ == '__main__':
    print(avaliacao_teste)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV3_avalia_teste['Preco_Original'])
    plt.plot(modeloV3_avalia_teste['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV3_teste = PlotResiduos(modeloV3_avalia_teste)
    residuosV3_teste.plot_residuos()


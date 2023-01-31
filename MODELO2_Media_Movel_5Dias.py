
'''
Modelo 2 - Média Móvel de 5 dias.
Treino e Teste do segundo modelo.
'''


import matplotlib.pyplot as plt
import numpy as np
from Tratamento_Dados import treino, treino_diferenciado, teste, teste_diferenciado
from Modulos.FUNCAO_Avaliando_Modelos import AvaliandoModelos
from Modulos.FUNCAO_Retomando_Valores_Previsao import retomando_valor_previsto
from Modulos.CLASSE_Plot_Erro import PlotResiduos
from MODELO1_Shift import avaliacao_treino, avaliacao_teste


                # Avaliando em Treino #
modeloV2_MM_treino = treino_diferenciado[['preco_reais']]
modeloV2_MM_treino.columns = ['Observado']
modeloV2_MM_treino['Previsto'] = modeloV2_MM_treino.rolling(5).mean()
modeloV2_MM_treino.dropna(inplace = True)

modeloV2_avalia_treino = retomando_valor_previsto(treino['preco_reais'], modeloV2_MM_treino['Previsto'])

avaliacao_treino['ModeloV2_MM_5Dias'] = AvaliandoModelos(modeloV2_avalia_treino['Preco_Original'],
                                                         modeloV2_avalia_treino['Preco_Previsto'])

if __name__ == '__main__':
    print(avaliacao_treino)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV2_avalia_treino['Preco_Original'])
    plt.plot(modeloV2_avalia_treino['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV2_treino = PlotResiduos(modeloV2_avalia_treino)
    residuosV2_treino.plot_residuos()

                    # Avaliando em Teste #
modeloV2_MM_teste = teste_diferenciado[['preco_reais']]
modeloV2_MM_teste.columns = ['Observado']

hist = [modeloV2_MM_treino.iloc[i, 0] for i in range(len(modeloV2_MM_treino))]
lista_previsao = []

for t in range(len(modeloV2_MM_teste)):
    yhat = np.mean(hist[-5:])
    obs = modeloV2_MM_teste.iloc[t, 0]
    lista_previsao.append(yhat)
    hist.append(obs)

modeloV2_MM_teste['Previsto'] = lista_previsao

modeloV2_avalia_teste = retomando_valor_previsto(teste['preco_reais'], modeloV2_MM_teste['Previsto'])

avaliacao_teste['ModeloV2_MM_5Dias'] = AvaliandoModelos(modeloV2_avalia_teste['Preco_Original'],
                                                        modeloV2_avalia_teste['Preco_Previsto'])
if __name__ == '__main__':
    print(avaliacao_teste)

if __name__ == '__main__':
    plt.figure(figsize = (8, 6))
    plt.plot(modeloV2_avalia_teste['Preco_Original'])
    plt.plot(modeloV2_avalia_teste['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV2_teste = PlotResiduos(modeloV2_avalia_teste)
    residuosV2_teste.plot_residuos()



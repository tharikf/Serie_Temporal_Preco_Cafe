
'''
Modelo 1 - Shift
Treino e Teste do primeiro modelo.
'''

import matplotlib.pyplot as plt
from Tratamento_Dados import treino, treino_diferenciado, teste, teste_diferenciado
from Modulos.FUNCAO_Avaliando_Modelos import AvaliandoModelos
from Modulos.FUNCAO_Retomando_Valores_Previsao import retomando_valor_previsto
from Modulos.CLASSE_Plot_Erro import PlotResiduos


                    # Avaliando em Treino #
modeloV1_shift_treino = treino_diferenciado[['preco_reais']]
modeloV1_shift_treino.columns = ['Observado']
modeloV1_shift_treino['Previsto'] = modeloV1_shift_treino.shift()
modeloV1_shift_treino.dropna(inplace = True)

modeloV1_avalia_treino = retomando_valor_previsto(treino['preco_reais'], modeloV1_shift_treino['Previsto'])

avaliacao_treino = AvaliandoModelos(modeloV1_avalia_treino['Preco_Original'],
                                    modeloV1_avalia_treino['Preco_Previsto'],
                                    nome_col = 'ModeloV1_Shift', nome_indice = 'Treino')

if __name__ == '__main__':
    print(avaliacao_treino)

if __name__ == '__main__':
    plt.figure(figsize = (12, 8))
    plt.plot(modeloV1_avalia_treino['Preco_Original'])
    plt.plot(modeloV1_avalia_treino['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV1_treino = PlotResiduos(modeloV1_avalia_treino)
    residuosV1_treino.plot_residuos()

                    # Avaliando em Teste #
modeloV1_shift_teste = teste_diferenciado[['preco_reais']]
modeloV1_shift_teste.columns = ['Observado']

hist = [modeloV1_shift_treino.iloc[i, 0] for i in range(len(modeloV1_shift_treino))]
lista_previsao = []

for t in range(len(modeloV1_shift_teste)):
    yhat = hist[-1]
    obs = modeloV1_shift_teste.iloc[t, 0]
    lista_previsao.append(yhat)
    hist.append(obs)

modeloV1_shift_teste['Previsto'] = lista_previsao


modeloV1_avalia_teste = retomando_valor_previsto(teste['preco_reais'], modeloV1_shift_teste['Previsto'])

avaliacao_teste = AvaliandoModelos(modeloV1_avalia_teste['Preco_Original'],
                                   modeloV1_avalia_teste['Preco_Previsto'],
                                   nome_col = 'ModeloV1_Shift', nome_indice = 'Teste')

if __name__ == '__main__':
    print(avaliacao_teste)

if __name__ == '__main__':
    plt.figure(figsize = (12, 8))
    plt.plot(modeloV1_avalia_teste['Preco_Original'])
    plt.plot(modeloV1_avalia_teste['Preco_Previsto'])
    plt.title('Preço da saca de 60kg líquido - Preco Original x Preco Previsto')
    plt.ylabel('')
    plt.show()

if __name__ == '__main__':
    residuosV1_teste = PlotResiduos(modeloV1_avalia_teste)
    residuosV1_teste.plot_residuos()





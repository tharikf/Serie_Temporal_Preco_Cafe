
'''
Essa função realiza a transformação de volta de dados previstos no dataset diferenciado para a escala original.
'''


import pandas as pd

'''
Retoma valores para os outros modelos.
'''
def retomando_valor_previsto(dataframe_original, dataframe_diferenciado):
    
    # Lista Vazia
    lista_vazia = []
    
    # Voltando valores para escala normal (sem diferenciação)
    for data, valor_original_df, valor_original, previsao_diferenciada in zip(dataframe_original.iloc[1:,].index, dataframe_original.iloc[1:,], dataframe_original, dataframe_diferenciado):
        valor_previsto = round((valor_original + previsao_diferenciada), 2)
        lista_vazia.append([data, valor_original_df, valor_previsto])
    
    df_resultados = pd.DataFrame(lista_vazia)
    df_resultados.columns = ['Data', 'Preco_Original', 'Preco_Previsto']
    df_resultados.set_index('Data', inplace = True)
    return df_resultados


'''
Essa função realiza a transformação de volta de dados previstos no dataset diferenciado para a escala original NO MODELO MÉDIAS MÓVEIS DE 5 DIAS
'''
def recuperando_valores_MM5(serie_original, serie_diferenciada, treino = True):
    
    lista_resultados = []
    
    if treino:
        for data, valor_original, valor_anterior_original, valor_previsto in zip(serie_original.iloc[5:,].index,
                                                                                 serie_original.iloc[5:, ],
                                                                                 serie_original.iloc[4:, ],
                                                                                 serie_diferenciada):
            valor_recuperado = round(valor_anterior_original + valor_previsto, 2)
            lista_resultados.append([data, valor_original, valor_recuperado])
    else:
        for data, valor_original, valor_anterior_original, valor_previsto in zip(serie_original.iloc[1:,].index,
                                                                                 serie_original.iloc[1:, ],
                                                                                 serie_original.iloc[0:, ],
                                                                                 serie_diferenciada):
            valor_recuperado = round(valor_anterior_original + valor_previsto, 2)
            lista_resultados.append([data, valor_original, valor_recuperado])
        
    
    df_resultados = pd.DataFrame(lista_resultados)
    df_resultados.columns = ['Data', 'Preco_Original', 'Preco_Previsto']
    df_resultados.set_index('Data', inplace = True)
    return df_resultados


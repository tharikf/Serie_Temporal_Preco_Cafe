
'''
Essa função realiza a transformação de volta de dados previstos no dataset diferenciado para a escala original.
'''


import pandas as pd

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





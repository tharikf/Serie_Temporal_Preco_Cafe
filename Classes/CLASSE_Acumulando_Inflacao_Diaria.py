
'''
Classe que obtém dados da inflação pela API do Banco Central e acumula os valores mensais para diários.
'''

import pandas as pd
from bcb import sgs

class AcumulandoInflacaoDiaria:

    def __init__(self, indice, numero_serie, inicio, fim):
        self.indice = indice
        self.numero_serie = numero_serie
        self.inicio = inicio
        self.fim = fim
        
        self.inflacao_diaria_dataframe = None
        self.importando_dados_api()

    
    def importando_dados_api(self):
        
        # Obtendo dados da API
        self.df_inflacao = sgs.get({self.indice : self.numero_serie}, start = self.inicio, end = self.fim)

        # Retirando a coluna do indice para realizar alteracoes
        self.df_inflacao = self.df_inflacao.reset_index()

        # Renomeando colunas
        self.df_inflacao.columns = ['Data', self.indice]
    

    def convertendo_inflacao_mensal_para_diaria(self):

        # Dias para cada mes
        meses_31 = [1, 3, 5, 7, 8, 10, 12]
        meses_30 = [4, 6, 9, 11]
        meses_28 = [2]

        # Lista vazia para adicionar os resultados
        lista_resultados = []

        # Convertendo taxa mensal para diária
        for mes, data, taxa in zip(self.df_inflacao['Data'].dt.month, self.df_inflacao['Data'], self.df_inflacao[self.indice]):
            if(mes in meses_31):
                inflacao_diaria = round((((1 + (taxa / 100)) ** (1 / 31)) - 1), 6)
                lista_resultados.append([data, inflacao_diaria])
            elif(mes in meses_30):
                inflacao_diaria = round((((1 + (taxa / 100)) ** (1 / 30)) - 1), 6)
                lista_resultados.append([data, inflacao_diaria])
            else:
                inflacao_diaria = round((((1 + (taxa / 100)) ** (1 / 28)) - 1), 6)
                lista_resultados.append([data, inflacao_diaria])
        
        # Colocando os resultados em um DataFrame
        self.inflacao_diaria_dataframe = pd.DataFrame(lista_resultados)
        self.inflacao_diaria_dataframe.columns = ['Data', 'Taxa_Diaria']
        self.inflacao_diaria_dataframe['Data'] = self.inflacao_diaria_dataframe['Data'].dt.to_period('M')

        return self.inflacao_diaria_dataframe








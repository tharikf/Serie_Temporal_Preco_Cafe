
'''
Módulo que realiza o tratamento dos dados para posterior análise.
'''

# Manipulação dos Dados
import numpy as np
import pandas as pd

# Visualização
import matplotlib.pyplot as plt
import seaborn as sns

# Funcoes
from Modulos.FUNCAO_Limpa_Dados import limpando_dados

# Carregando os Dados
df = pd.read_excel('serie_preco_cafe.xls')

# Aplica função que limpa os dados
df = limpando_dados(df)

# Dividindo dados em treino e teste
treino = df.iloc[:749, :]
teste = df.iloc[749:, :]

# Diferenciado os dados para obter estacionariedade
treino_diferenciado = treino.diff().dropna()
teste_diferenciado = teste.diff().dropna()


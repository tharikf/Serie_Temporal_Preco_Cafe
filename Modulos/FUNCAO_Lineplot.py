
'''
Função que cria um padrão para o gráfico de linha que é recorrente no projeto.
'''

import pandas as pd

# Visualização
import matplotlib.pyplot as plt
import seaborn as sns


def lineplot(x, y, titulo, ylabel = None, *args):
    
    fig, ax = plt.subplots(figsize = (12, 10))
    sns.lineplot(x = x, y = y)
    
    for i in range(0, len(args), 2):
        if i+1 < len(args):
            sns.lineplot(args[i], args[i+1])
            
    ax.set_title(titulo)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.ylabel(ylabel)
    plt.show()








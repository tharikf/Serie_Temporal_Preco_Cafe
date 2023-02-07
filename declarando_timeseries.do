
* Importando os dados
import delimited C:\Users\thari\Documents\Cursos\Portfolio\Serie_Temporal_Preco_Soja\df_soja_stata.csv

* Criando a variável como tempo
generate Data = date(data, "YMD")

* Formatando
format %td Data

* Declarando a variavel como variavel de tempo
tsset Data, daily

* Excluindo variavel
drop data

* Gerando a primeira diferenca
gen preco_diferenciado = preco_reais[_n] - preco_reais[_n-1]

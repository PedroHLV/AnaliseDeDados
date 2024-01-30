import pandas as pd
import plotly_express as px

dados = pd.read_excel("vendas.xlsx")

# Linhas iniciais
cabecalho = dados.head()

# Linhas finais
linhas_finais = dados.tail()

# Quantidade de linhas e colunas
colunas_linhas = dados.shape

# Verificar tipo de dados
tipo_dados = dados.info()

# Selecionar uma coluna
# preco = dados.preco

# Gerando Esatisticas
preco = dados.preco.describe()

# Total de vendas por loja
vendas = dados.loja.value_counts()

# Total de vendas por cidade
vendas_cidade = dados.cidade.value_counts()

# Total de vendas por forma de pagamento
forma_pagamento = dados.forma_pagamento.value_counts()

# Agrupamento de Dados
# Faturamento por loja, pegando a soma
faturamento_loja = dados.groupby("loja").preco.sum()

# Faturamento por estado, cidade, loja pegando a media. Armazenando isso em um excel
# faturamento_estado = dados.groupby(["estado", "cidade", "loja"]).preco.mean().to_excel("Faturamento-Estado-Cidade.xlsx")

# Visualização de dados em gráfico
colunas = ['loja', 'estado', 'cidade', 'tamanho']
for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco', title=f"Faturamento por {coluna}", text_auto=True, color="forma_pagamento")
    grafico.write_html(f"grafico-{coluna}.hmtl")
    grafico.show()
import streamlit as st
import pandas as pd
import plotly.express as px

# Rodar com streamlit run .\app.py

# Carregar dados
dados = pd.read_excel("vendas.xlsx")

# Título do Dashboard
st.title('Dashboard de Vendas')

# Subtítulo
st.subheader('Estatísticas Gerais')

# Mostrar linhas iniciais e finais
st.write('**Linhas iniciais:**')
st.write(dados.head())

st.write('**Linhas finais:**')
st.write(dados.tail())

# Quantidade de linhas e colunas
st.write('**Quantidade de linhas e colunas:**')
st.write(dados.shape)

# Verificar tipo de dados
st.write('**Tipo de dados:**')
st.write(dados.info())

# Mostrar estatísticas do preço
st.write('**Estatísticas do preço:**')
st.write(dados['preco'].describe())

# Total de vendas por loja
st.write('**Total de vendas por loja:**')
st.write(dados['loja'].value_counts())

# Total de vendas por cidade
st.write('**Total de vendas por cidade:**')
st.write(dados['cidade'].value_counts())

# Total de vendas por forma de pagamento
st.write('**Total de vendas por forma de pagamento:**')
st.write(dados['forma_pagamento'].value_counts())

# Faturamento por loja
st.subheader('Faturamento por Loja')
faturamento_loja = dados.groupby("loja")['preco'].sum()
st.write(faturamento_loja)

# Visualização de dados em gráfico
colunas = ['loja', 'estado', 'cidade', 'tamanho']
for coluna in colunas:
    grafico = px.histogram(dados, x=coluna, y='preco', title=f"Faturamento por {coluna}", text_auto=True, color="forma_pagamento")
    st.plotly_chart(grafico)


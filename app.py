import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Relatorio de vendas", layout="wide")
st.title("Dashboard de Vendas - Oficial")

#Tentativa de carregamento dos dados
try:
    df = pd.read_csv("vendas.csv")
    
    #Mostrando a tabela
    st.subheader("Visão geral dos dados")
    st.dataframe(df)

    st.subheader("Vendas por dia da semana")
    coluna_texto = "Dia"

    if coluna_texto in df.columns:
        dados_grafico = df.set_index(coluna_texto)
        st.bar_chart(dados_grafico)

    else:
     st.error(f"Não encontrei a coluna '{coluna_texto}' no CSV.")
    
     #Cria um grafico simples se houver colunas numericas

except FileNotFoundError:
    st.error("Erro: O arquivo 'vendas.csv' nao foi encontrado na pasta")

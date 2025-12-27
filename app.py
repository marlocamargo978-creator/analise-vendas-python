import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Relatorio de vendas", layout="wide")
st.title("Dashboard de Vendas")

#Tentativa de carregamento dos dados
try:
    df = pd.read_csv("vendas.csv")

    st.subheader("Resumo da Semana")
    col1, col2, col3 = st.columns(3)

    #Calculando os totais
    total_vendas = df["Vendas"].sum()
    total_clientes = df["Clientes"].sum()
    media_vendas = df["Vendas"].mean()

    #Mostrando cartoes
    col1.metric("Total de Vendas", f"R$ {total_vendas:,.2f}")
    col2.metric("Total de Clientes", total_clientes)
    col3.metric("Média por Dia", f"R$ {media_vendas:,.2f}")

    st.divider() #Uma linha divisoria
    
    #Mostrando a tabela
    st.subheader("Visão geral dos dados")
    st.dataframe(df, hide_index=True)
    st.subheader("Vendas por dia da semana")
    
    coluna_texto = 'Dia'

    if coluna_texto in df.columns:
        dados_grafico = df.set_index(coluna_texto)
        st.bar_chart(dados_grafico)
    else:
        st.error(f"Não encontrei a coluna '{coluna_texto}' no CSV.")
    
except FileNotFoundError:
    st.error("Erro: O arquivo 'vendas.csv' nao foi encontrado na pasta")

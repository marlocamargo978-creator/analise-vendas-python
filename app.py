import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Relatorio de vendas", layoute="wide")

#Tentativa de carregamento dos dados
try:
    df = pd.read_csv("vendas.csv")
    
    #Mostrando a tabela
    st.subheader("Visão geral dos dados")
    st.dataframe(df.head())
    
    st.subheader("Vendas por categoria/produto")
    
    #Cria um grafico simples se houver colunas numericas
    st.bar_chart(df.select_dtypes(include=['float', 'int']))

except FileNotFoundError:
    st.error("Erro: O arquivo 'vendas.csv' nao foi encontrado na pasta")


import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Relatorio de vendas", layout="wide")

#Tentativa de carregamento dos dados
try:
    df = pd.read_csv("vendas.csv")
    
    #Mostrando a tabela
    st.subheader("Visão geral dos dados")
    st.dataframe(df.head())
    
    st.subheader("Vendas por categoria/produto")
    

except FileNotFoundError:
    st.error("Erro: O arquivo 'vendas.csv' nao foi encontrado na pasta")


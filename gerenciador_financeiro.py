import streamlit as st
import pandas as pd
from app import *
from components import sidebar, dashboards, extratos


st.title('Gerenciador Financeiro')
st.write('Bem-vindo ao seu gerenciador financeiro pessoal!')


# DataFrames and Streamlit Caching
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path, index_col=0, parse_dates=True)

df_receitas = load_data("df_receitas.csv")
df_despesas = load_data("df_despesas.csv")
list_receitas = load_data("df_cat_receita.csv")
list_despesas = load_data("df_cat_despesa.csv")

# Layout
st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Sidebar")
    # Add your sidebar components here

# Page content
main_column = st.beta_container()

if st.sidebar.button("Dashboards"):
    with main_column:
        dashboards.layout(df_receitas, df_despesas, list_receitas, list_despesas)

if st.sidebar.button("Extratos"):
    with main_column:
        extratos.layout()

def main():
    st.title('Gerenciador Financeiro')
    st.write('Bem-vindo ao seu gerenciador financeiro pessoal!')
    
    
# Barra lateral
menu = st.sidebar.selectbox('Menu', ['Visão Geral', 'Despesas', 'Receitas'])

if menu == 'Visão Geral':
    st.subheader('Visão Geral')
    # Adicione código para exibir uma visão geral das finanças

elif menu == 'Despesas':
    st.subheader('Despesas')
    # Adicione código para adicionar/editar/excluir despesas

elif menu == 'Receitas':
    st.subheader('Receitas')
    # Adicione código para adicionar/editar/excluir receitas

if __name__ == '__main__':
    main()

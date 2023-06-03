import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
data = [...]  # Insira aqui seus dados

# Converter os dados para DataFrame
df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data']).dt.date
df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'
df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'
df = df.fillna('-')

# Layout
st.title("Tabela de Despesas")
st.dataframe(df)

# Gráfico de barras
df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
fig = px.bar(df_grouped, x='Categoria', y='Valor', title="Despesas Gerais")
st.plotly_chart(fig)

# Total de despesas
valor_total = df['Valor'].sum()
st.write(f"Total de despesas: R$ {valor_total}")

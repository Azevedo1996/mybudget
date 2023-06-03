import streamlit as st
from datetime import datetime, date

# Layout
st.title("MyBudget")
st.subheader("By ASIMOV")
st.markdown("---")

# Seção PERFIL ------------------------
st.markdown("## Selecionar Perfil")

avatar_change = st.button("Select Avatar")
if avatar_change:
    st.info("Avatar selected")

# Seção + NOVO ------------------------
st.markdown("## Novo")

col1, col2 = st.beta_columns(2)

novo_receita = col1.button("+ Receita")
if novo_receita:
    st.info("Add Receita")

novo_despesa = col2.button("+ Despesa")
if novo_despesa:
    st.info("Add Despesa")

# Seção NAV ------------------------
st.markdown("---")
st.sidebar.markdown("## Navigation")
option = st.sidebar.radio("Go to", ("Dashboard", "Extratos"))

if option == "Dashboard":
    st.info("Go to Dashboard")
elif option == "Extratos":
    st.info("Go to Extratos")

# Theme Changer
theme = st.sidebar.radio("Theme", ("QUARTZ", "Other Themes"))
st.write(f"Selected Theme: {theme}")

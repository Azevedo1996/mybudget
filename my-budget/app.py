import streamlit as st

st.set_page_config(page_title="Meu Aplicativo", page_icon=":chart_with_upwards_trend:")

# Defina estilos personalizados
estilos = """
<style>
    /* Adicione seus estilos personalizados aqui */
</style>
"""

# Carregue os estilos e temas externos
css_urls = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://fonts.googleapis.com/icon?family=Material+Icons"
]

for url in css_urls:
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# Aplicar estilos personalizados
st.markdown(estilos, unsafe_allow_html=True)

# Defina o título da página
st.title("Meu Aplicativo")

# Resto do seu código Streamlit aqui

import streamlit as st
from datetime import date, datetime

# =========  Componentes  =========== #
calendario1 = st.date_input("Selecione uma data", min_value=datetime.today(), max_value=date(2030, 12, 31), value=datetime.today())

calendario2 = st.date_input("Selecione uma data", min_value=datetime.today(), max_value=date(2030, 12, 31), value=datetime.today())

# =========  Callbacks  =========== #
@st.cache
def formatar_data(date_value):
    string_prefix = 'Selecionado: '
    if date_value is not None:
        date_object = date.fromisoformat(str(date_value))
        date_string = date_object.strftime('%d %B, %Y')
        return string_prefix + date_string

output_container_datepicker = formatar_data(calendario1)
st.write(output_container_datepicker)

output_container_datepicker2 = formatar_data(calendario2)
st.write(output_container_datepicker2)

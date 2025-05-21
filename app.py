import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.stats import chi2_contingency

st.title('Mi segunda publicación')
st.header('Introducción')
st.write('Esta es la primera publicación')
st.write('-_-')
st.write('^-^')

datos = sns.load_dataset('penguins')

datos.drop_duplicates(inplace=True)
datos = datos.dropna()

st.write("Longitud de la aleta por especie")
st.write("Shapiro-Wilk")
for grupo in datos["species"].unique():
    datos_grupo = datos[datos["species"] == grupo]["flipper_length_mm"]
    estadistico, p_value = stats.shapiro(datos_grupo)
    if (p_value > 0.05):
        aux = "Sí"
    elif (p_value < 0.05):
        aux = "No"
    else:
        aux = "-"
    st.write("El valor p (", grupo,") es: ", p_value, aux, "tiene una distribución normal")

st.plotly_chart(px.violin(datos, y = "flipper_length_mm", color = "species", box=True, title="Longitud de la aleta por especie"))



import pandas as pd
import plotly.express as px
import streamlit as st
import pickle as pkl
import numpy as np
 
gpa = pd.read_csv('gpa.csv')
 

st.title("Promedio en la U")
 
with open("model.pickle", "rb") as m:
    modelo = pkl.load(m)
 
Tab1, Tab2, Tab3 = st.tabs(['Analisis Univariado', 'Analisis Bivariado', 'Modelo'])
colores= ['#81D2C7', '#B5BAD0', '#7389AE', '#416788']
with Tab1:

    st.subheader("Estadísticas descriptivas - Variables numéricas")
    st.dataframe(gpa[['Prom_Universidad', 'ACT', 'Prom_Colegio', 'Capar_clase']].describe())

    st.subheader("Distribución de variables numéricas")
 
    fig1 = px.histogram(gpa, x='Prom_Universidad', title ='Promedio en la U', color_discrete_sequence=[colores[0]])
    st.plotly_chart(fig1)

    fig2 = px.histogram(gpa, x='ACT',title= 'Puntaje ACT',color_discrete_sequence=[colores[1]])
    st.plotly_chart(fig2)

    fig3 = px.histogram(gpa, x='Prom_Colegio', title= 'Promedio en el colegio',color_discrete_sequence=[colores[2]])
    st.plotly_chart(fig3)

    fig4 = px.histogram(gpa, x='Capar_clase', title = 'Promedio de veces que faltó a clase',color_discrete_sequence=[colores[3]])
    st.plotly_chart(fig4)
 
 
 
with Tab2:
    st.subheader("Relación entre variables y el promedio ponderado en la U")
 
    fig1 = px.scatter(gpa, x='ACT', y='Prom_Universidad', title='Promedio en la U vs Puntaje ACT', color="Prom_Universidad", color_continuous_scale= 'blues')
    st.plotly_chart(fig1)
 
    fig2 = px.scatter(gpa, x='Prom_Colegio', y='Prom_Universidad', 
    title='Promedio en la U vs Promedio en el colegio', color="Prom_Universidad", color_continuous_scale= 'purples')
  
    st.plotly_chart(fig2)
 
    fig3 = px.scatter(gpa, x='Capar_clase', y='Prom_Universidad',color="Prom_Universidad", color_continuous_scale= 'purd',title='Promedio en la U vs Cant. veces que faltó a clase')
    st.plotly_chart(fig3)
 
with Tab3:
    st.title("Modelo")
 
    Prom_Colegio = st.slider("Promedio en el colegio", 0, 5)
 
    ACT = st.slider("Puntaje ACT", 1, 36)
 
    Capar_clase= st.slider("Cantidad de veces en promedio que faltó a clase", 0, 10)
 
 
    if st.button ("Predecir"):
        Predecir = modelo.predict(np.array([[ACT, Prom_Colegio, Capar_clase]]))
        st.write(f"Tu promedio sería: {round(Predecir [0], 2)}")
 
print(10)

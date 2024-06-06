import pandas as pd
import plotly.express as px
import streamlit as st
        
vehicles = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
     st.write('Scatter plot')
            
            # crear un histograma
     fig = px.histogram(vehicles, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)
     
st.header('Vehicles type by manufacturer')

disp_button = st.button('Construir grafico de dispersión')#Crea un boton para generar un grafico de dispersión.

if disp_button:
    st.write('Scatter plot')
    #Crea un grafico de dispersión
    fig1 = px.scatter(vehicles, x='odometer', y='price')
    #Mostrar grafico de dispersión interactivo
    st.plotly_chart(fig1, use_container_width=True)
     
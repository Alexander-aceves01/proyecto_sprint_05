import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown('# Análisis de venta')

# Leer los datos
vehicles = pd.read_csv('vehicles_us.csv')

# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón del histograma
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_hist = px.histogram(vehicles, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.checkbox('Construir gráfico de dispersión', key='scatter')

# Si la casilla del gráfico de dispersión está marcada
if scatter_checkbox:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(vehicles, x="odometer", y="price", title="Precio vs. Kilometraje")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)


import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')#lendo dados

st.header('dash -sprint 5')
hist_button = st.button('criar histograma') #criar botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

#grafico de dispersão
disp_button = st.button('criar grafico dispersão') #criar botão

if disp_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um grafico de dispersão
    fig = plt.scatter(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

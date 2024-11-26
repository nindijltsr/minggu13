import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Memuat model prediksi harga mobil dari file .sav
model = pickle.load(open('model_regresi.sav', 'rb'))

st.title('Prediksi Harga Mobil')
st.header("Dataset")

df1 = pd.read_csv('car_price.csv')
st.dataframe(df1)

st.write("Grafik Highway-mpg")
chart_highwaympg = df1['highwaympg']
st.line_chart(chart_highwaympg)

st.write("Grafik Curbweight")
chart_curbweight = df1['curbweight']
st.line_chart(chart_curbweight)

st.write("Grafik Horsepower")
chart_horsepower = df1['horsepower']
st.line_chart(chart_horsepower)

highwaympg = st.number_input('Masukkan Highway MPG', min_value=0, max_value=100, value=30)
curbweight = st.number_input('Masukkan Curbweight', min_value=0, max_value=10000, value=2500)
horsepower = st.number_input('Masukkan Horsepower', min_value=0, max_value=1000, value=150)

if st.button('Prediksi'):
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
    
    harga_mobil_float = float(car_prediction[0])  

    harga_mobil_juta = harga_mobil_float * 1000  

    harga_mobil_formatted = f"Rp {harga_mobil_juta:,.2f}"
    st.write(f'Harga Mobil yang diprediksi adalah: {harga_mobil_formatted}')

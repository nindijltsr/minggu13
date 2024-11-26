import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Memuat model prediksi harga mobil dari file .sav
model = pickle.load(open('model_regresi.sav', 'rb'))

st.title('Prediksi Harga Mobil')

# Memuat dan menampilkan dataset
df1 = pd.read_csv('car_price.csv')
st.header("Dataset")
st.dataframe(df1)

# Visualisasi data dengan line chart
st.write("Grafik Highway-mpg")
chart_highwaympg = df1['highwaympg']
st.line_chart(chart_highwaympg)

st.write("Grafik Curbweight")
chart_curbweight = df1['curbweight']
st.line_chart(chart_curbweight)

st.write("Grafik Horsepower")
chart_horsepower = df1['horsepower']
st.line_chart(chart_horsepower)

# Menggunakan slider untuk input fitur mobil
highwaympg = st.slider('Pilih Highway MPG', min_value=0, max_value=100, value=30)
curbweight = st.slider('Pilih Curbweight', min_value=0, max_value=10000, value=2500)
horsepower = st.slider('Pilih Horsepower', min_value=0, max_value=1000, value=150)

# Tombol untuk memulai prediksi
if st.button('Prediksi'):
    # Melakukan prediksi dengan model
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
    
    # Menghitung harga mobil dan menampilkannya dalam format yang sesuai
    harga_mobil_float = float(car_prediction[0])  
    harga_mobil_juta = harga_mobil_float * 1000  
    harga_mobil_formatted = f"Rp {harga_mobil_juta:,.2f}"
    
    st.write(f'Harga Mobil yang diprediksi adalah: {harga_mobil_formatted}')

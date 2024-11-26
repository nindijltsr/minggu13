import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from wordcloud import WordCloud
import pickle 

# Membaca dataset
df_mobil = pd.read_csv("car_price.csv")
st.write("Data Mobil")
st.write(df_mobil)

missing_data = df_mobil.isnull().sum()
st.write("Missing Data")
st.write(missing_data)

st.write("Statistik Deskriptif")
st.write(df_mobil.describe())

st.write("Tipe Data")
st.write(df_mobil.dtypes)

fig, ax = plt.subplots(figsize=(10, 4))
ax.set_title('Car Price Distribution Plot')
sns.histplot(df_mobil.price, ax=ax)
st.pyplot(fig)

car_counts = df_mobil['CarName'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
car_counts.plot(kind="bar", ax=ax)
ax.set_title("CarName Distribution")
ax.set_xlabel("CarName")
ax.set_ylabel("Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

car_names = ' '.join(df_mobil['CarName'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(car_names)
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Car Name Word Cloud')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df_mobil['highwaympg'], df_mobil['price'])
ax.set_xlabel('highwaympg')
ax.set_ylabel('price')
st.pyplot(fig)

x = df_mobil[['highwaympg','curbweight','horsepower']]
y = df_mobil['price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model_regresi = LinearRegression()
model_regresi.fit(X_train, y_train)

model_regresi_pred = model_regresi.predict(X_test)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X_test.iloc[:, 0], y_test, label='Actual Prices', color='blue')
ax.scatter(X_test.iloc[:, 0], model_regresi_pred, label='Predicted Prices', color='red')
ax.set_xlabel('highwaympg')
ax.set_ylabel('price')
ax.legend()
st.pyplot(fig)

X_input = pd.DataFrame([[32, 2338, 75]], columns=['highwaympg', 'curbweight', 'horsepower'])
prediksi_harga = model_regresi.predict(X_input)
st.write(f"Prediksi harga mobil: {prediksi_harga[0]:.2f}")

mae = mean_absolute_error(y_test, model_regresi_pred)
mse = mean_squared_error(y_test, model_regresi_pred)
rmse = np.sqrt(mse)

st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
st.write(f"Mean Squared Error (MSE): {mse:.2f}")
st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Simpan model menggunakan pickle dengan ekstensi .sav
with open('model_regresi.sav', 'wb') as model_file:
    pickle.dump(model_regresi, model_file)

st.write("Model berhasil disimpan sebagai 'model_regresi.sav'")

# Muat model yang disimpan dengan ekstensi .sav
with open('model_regresi.sav', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
    
new_prediction = loaded_model.predict(X_input)
st.write(f"Prediksi harga mobil menggunakan model yang dimuat: {new_prediction[0]:.2f}")

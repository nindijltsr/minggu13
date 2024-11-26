import streamlit as st
# A. Streamlit Dasar

# # NOMOR 1
# st.write("Hello world")

# # NOMOR 2
# st.header('st.button')

# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

# # NOMOR 3
# st.title("this is the app title")
# st.markdown("this is the markdown")
# st.header("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x = 2021")

# # NOMOR 4
# agree = st.checkbox("yes")
# st.button("Click")
# genre = st.radio(
#     "Pick your gender",
#     ["Male", "Female"],
#     index=None,
# )
# option = st.selectbox(
#     "Pick your gender",
#     ("Male", "Female"),
# )
# option = st.selectbox(
#     "chose a planet",
#     ("Merkurius", "Venus", "Bumi", "Mars", "Jupiter", "Saturnus", "Uranus", "Neptunus" ),
#     index=None,
#     placeholder="Choose an option",
# )
# pick = st.select_slider(
#     "Pick a mark",
#     options=[
#         "Bad",
#         "Good",
#         "Excellent",
#     ]
# )
# number = st.select_slider(
#     "Pick a number range",
#     options=list(range(51)),             
# )

# NOMOR 5
# number = st.number_input("Pick a number")
# title = st.text_input("Email address", "")

# import datetime
# d = st.date_input("Travelling date", datetime.date(2019, 7, 6))
# t = st.time_input("School time", datetime.time(8, 45))
# txt = st.text_area(
#     "Description",
#     "",
# )

# import pandas as pd
# from io import StringIO

# uploaded_file = st.file_uploader("Upload a photo")
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     string_data = stringio.read()
#     st.write(string_data)

#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

#     uploaded_files = st.file_uploader(
#     "Choose a CSV file", accept_multiple_files=True
# )
# color = st.color_picker("Pick A Color")

# # Nomor 6
# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('Halo')
# st.write('Hello, *World!* 😎')
# st.write(1234)

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# st.write(df)

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# df2 = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c']
# )
# c = alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
# )
# st.write(c)

# NOMOR 7
# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=['x', 'y']
# )
# st.line_chart(df)

# NOMOR 8
import streamlit as st
import pandas as pd

def main():
    # Sidebar menu
    menu = ["Home", "Image", "Dataset", "Graph"]
    choice = st.sidebar.selectbox("Select Page", menu)

   # Halaman Home
    if choice == "Home":
        st.title("Home")
        st.title("Selamat Datang di Restaurant Data Viewer!!")
        st.write("""
            Aplikasi ini dirancang untuk membantu Anda mengeksplorasi dan menganalisis data restoran secara interaktif.
            Anda dapat melihat informasi gambar terkait restoran, mengunggah dan menampilkan dataset restoran, 
            serta membuat visualisasi grafik yang menarik berdasarkan data yang tersedia.
        """)

    # Halaman Image
    elif choice == "Image":
        st.title("Image")
        # Menampilkan gambar
        st.image("data.jpeg", caption="Restaurant Data Image", use_container_width=True)

    # Halaman Dataset
    elif choice == "Dataset":
        st.title("Dataset")
        try:
            df = pd.read_csv("RestaurantData.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.error("Dataset 'RestaurantData.csv' tidak ditemukan. Pastikan file berada di direktori yang sama dengan skrip.")

    # Graph Page
    elif choice == "Graph":
        st.title("Graph")
        try:
            df = pd.read_csv("RestaurantData.csv")
            # Jumlah rating berdasarkan cuisine
            total_ratings_per_cuisine = df.groupby("Cuisine")["Number of Ratings"].sum().reset_index()
            st.write("Graph: Total Number of Ratings per Cuisine")
            st.bar_chart(total_ratings_per_cuisine.set_index("Cuisine"))
        except FileNotFoundError:
            st.error("Dataset 'RestaurantData.csv' tidak ditemukan.")
        except KeyError:
            st.error("Kolom 'Cuisine' atau 'Number of Ratings' tidak ditemukan dalam dataset.")

if __name__ == '__main__':
    main()

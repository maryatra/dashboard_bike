import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk mengimpor data
@st.cache_data
def load_data():
    data_df = pd.read_csv('D:\VSCode Project\.venv\Scripts\day.csv')
    return data_df

# Fungsi untuk melakukan pembersihan data
def clean_data(data_df):
    data_df['season'] = data_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    return data_df

# Fungsi untuk menampilkan gathering data
def gather_data(data_df):
    st.subheader("Gathering Data")
    st.write("Berikut merupakan dataset dari Bike Sharing pada skala hari")
    st.write(data_df)

# Fungsi untuk menampilkan assessing data
def assess_data(data_df):
    st.subheader("Assessing Data")
    st.write("Melakukan pemeriksaan parameter statistik menggunakan metode describe()")
    st.write(data_df.describe())

# Fungsi untuk menampilkan cleaning data
def clean_data_display(data_df):
    st.subheader("Cleaning Data")
    st.write("Mengubah nilai dari parameter 'season' menjadi nama musim")
    cleaned_data_df = clean_data(data_df.copy())
    st.write(cleaned_data_df)

# Fungsi untuk menjawab pertanyaan EDA
def eda_questions(data_df):
    st.subheader('Exploratory Data Analysis (EDA)')
    
    # Pertanyaan 1
    st.markdown("### Pertanyaan 1: Distribusi Peminjaman untuk Masing-masing Musim dan Kondisi Cuaca")
    st.write("Bagaimana distribusi peminjaman untuk masing-masing musim dan kondisi cuaca?")
    st.write("Melakukan pemetaan tabel menggunakan pivot table")
    data_df['season'] = data_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    data_musim = data_df.groupby(by=["season", "weathersit"]).agg({
        "casual": "nunique",
        "registered": "nunique"
    })
    st.write(data_musim)
    st.write('Grafik')
    data_musim['total'] = data_musim['casual'] + data_musim['registered']
    fig, ax = plt.subplots()
    sns.barplot(data=data_musim, x="season", y="total", hue="weathersit", errorbar=None, ax=ax)
    st.pyplot(fig)

    # Pertanyaan 2
    st.markdown("### Pertanyaan 2: Pengaruh Hari Kerja/Akhir Pekan terhadap Peminjaman untuk Setiap Musim")
    st.write("Pengaruh hari kerja/ akhir pekan terhadap peminjaman untuk setiap musim?")
    st.write("Melakukan pemetaan tabel menggunakan pivot table")
    data_holiday = data_df.groupby(by="season").agg({
        "casual": "nunique",
        "registered": "nunique",
    })
    st.write(data_holiday)
    st.write('Grafik')
    data_holiday['total'] = data_holiday['casual'] + data_holiday['registered']
    fig, ax = plt.subplots()
    sns.scatterplot(data=data_holiday, x='season', y='casual', ax=ax)
    sns.scatterplot(data=data_holiday, x='season', y='registered', ax=ax)
    ax.set_ylim(150, 190)
    st.pyplot(fig)

def main():
    st.title('Analisis Data Bike Sharing')
    data_df = load_data()
    
    menu = ["Gathering Data", "Assessing Data", "Cleaning Data", "Exploratory Data Analysis (EDA)"]
    choice = st.sidebar.selectbox("Pilihan Menu", menu)

    if choice == "Gathering Data":
        gather_data(data_df)
    elif choice == "Assessing Data":
        assess_data(data_df)
    elif choice == "Cleaning Data":
        clean_data_display(data_df)
    elif choice == "Exploratory Data Analysis (EDA)":
        eda_questions(data_df)
    
    # Kesimpulan
    st.sidebar.subheader('Kesimpulan')
    st.sidebar.write("Berdasarkan analisis yang dilakukan, dapat disimpulkan bahwa...")
    st.sidebar.write("Tambahan kesimpulan atau analisis lanjutan dapat ditambahkan di sini.")

if __name__ == "__main__":
    main()

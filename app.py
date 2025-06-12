import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Data", layout="wide")
st.title("📊 Aplikasi Analisis Data Sederhana dengan Grafik")

uploaded_file = st.file_uploader("📁 Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📄 Dataframe")
    st.dataframe(df)

    st.subheader("📈 Statistik Deskriptif")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    if numeric_cols:
        st.subheader("📊 Histogram Data Numerik")
        col = st.selectbox("Pilih kolom numerik", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("📉 Boxplot (Deteksi Outlier)")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[col], ax=ax2)
        st.pyplot(fig2)

        if len(numeric_cols) > 1:
            st.subheader("Corelation Heatmap")
            fig3, ax3 = plt.subplots(figsize=(8, 6))
            corr = df[numeric_cols].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
            st.pyplot(fig3)
    else:
        st.warning("Tidak ada kolom numerik yang tersedia untuk dianalisis.")
else:
    st.info("Silakan upload file CSV untuk dianalisis.")

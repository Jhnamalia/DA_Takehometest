import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Telco Churn Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title & Description
st.title("📊 Customer Insights & Business Performance Dashboard")
st.markdown("""
Selamat datang di **Telco Customer Churn Analysis Dashboard**.  
Proyek ini menganalisis data pelanggan Telco untuk memahami alasan pelanggan berhenti berlangganan (*churn*) dan memberikan wawasan strategis untuk meningkatkan retensi pelanggan.
""")

# Hero Image
image = Image.open("images/churn_example.png")
st.image(image, use_container_width=True)

# Navigation
st.subheader("📌 Halaman yang Tersedia")
st.markdown("""
1. **About Me** – Informasi pembuat proyek.
2. **Overview Project** – Latar belakang, tujuan, dan key business question.
3. **Data Understanding** – Penjelasan dataset & feature.
4. **Data Preparation** – Langkah pembersihan & transformasi data.
5. **EDA Visualisasi & Insight** – Analisis visual dan temuan penting.
6. **Business Recommendation** – Rekomendasi strategis untuk perusahaan.
7. **Tableau Dashboard** – Tampilan interaktif dari dashboard Tableau.
8. **Contact** – Informasi contact pembuat proyek.
""")
import streamlit as st
from PIL import Image

st.title("📄 Overview Project")

# =========================
# Business Understanding
# =========================
st.header("1️⃣ Business Understanding")
st.markdown("""
📌 Perusahaan telekomunikasi ingin memahami **pola perilaku pelanggan** dan **faktor penyebab churn**.  
Dengan analisis ini, perusahaan dapat menyusun strategi untuk **menekan churn rate** dan meningkatkan **retensi pelanggan**.

Dataset yang digunakan: **Telco Customer Churn** dari Kaggle 📊
Berisi data:
- Demografi pelanggan 👨‍👩‍👧‍👦
- Jenis layanan 📶
- Skor kepuasan pelanggan
- Status churn (Ya/Tidak)
""")
st.info("🎯 Tujuan utama: Memahami pola churn dan memberikan insight untuk strategi retensi pelanggan.")

st.divider()

# =========================
# Latar Belakang Masalah
# =========================
st.header("2️⃣ Latar Belakang Masalah")
st.markdown("""
⚠️ **Masalah yang dihadapi**:
- Tingginya tingkat churn mengurangi profit perusahaan 📉
- Belum ada analisis mendalam terhadap faktor penyebab churn
- Strategi retensi masih bersifat umum, belum personal

💡 **Pentingnya analisis churn**:
- Mengidentifikasi segmen pelanggan yang rawan churn
- Memberikan dasar untuk strategi promosi & penawaran khusus
""")

st.divider()

# =========================
# Tujuan Analisa
# =========================
st.header("3️⃣ Tujuan Analisa")
st.markdown("""
Analisis ini bertujuan untuk:
1. 🔍 Mengetahui distribusi churn berdasarkan karakteristik pelanggan.
2. 📊 Menggali hubungan antara demografi, layanan, dan churn.
3. 📝 Memberikan rekomendasi strategi retensi berdasarkan data.
""")

st.divider()

# =========================
# Key Business Questions
# =========================
st.header("4️⃣ Key Business Questions")
st.markdown("""
- 📌 Bagaimana distribusi churn pelanggan secara keseluruhan?
- 📌 Segmen pelanggan mana yang paling rentan churn?
- 📌 Jenis layanan dan kontrak mana yang memengaruhi churn?
- 📌 Bagaimana CLTV dan tenure berhubungan dengan churn?
- 📌 Apakah skor kepuasan pelanggan berpengaruh terhadap churn?
""")

st.divider()

# =========================
# Flow Diagram
# =========================
st.header("📊 Alur Analisis")
st.markdown("Berikut adalah langkah analisis yang dilakukan:")

flow_img = Image.open("images/project_flow_telco_no_model.png")
st.image(flow_img, caption="Flow Analisis Telco Customer Churn", use_container_width=True)

st.success("Dengan alur ini, analisis dapat menjawab pertanyaan bisnis dan memberikan rekomendasi berbasis data.")

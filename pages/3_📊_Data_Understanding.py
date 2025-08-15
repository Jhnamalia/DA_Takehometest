import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

st.title("📊 Data Understanding")

st.markdown("""
Dataset **Telco Customer Churn** ini digunakan untuk menganalisis faktor-faktor yang memengaruhi pelanggan berhenti berlangganan (*churn*).
Dataset berasal dari **Kaggle - IBM Telco Customer Churn** dan terdiri dari beberapa sheet Excel yang digabung menjadi satu tabel utuh.
""")

df = pd.read_csv("data/final_dataset.csv")  # file hasil merge & cleaning

# 1. Ringkasan Dataset
st.subheader("📌 Ringkasan Dataset")
st.markdown(f"""
- Jumlah baris: **{df.shape[0]:,}**
- Jumlah kolom: **{df.shape[1]:,}**
""")

# 2. Tipe Data
st.subheader("📂 Struktur Kolom & Tipe Data")
st.dataframe(df.dtypes.reset_index().rename(columns={"index": "Nama Kolom", 0: "Tipe Data"}))

# 3. Kategori Fitur
st.subheader("📋 Kategori Fitur")
st.markdown("""
- **Demografi Pelanggan**: `gender`, `age`, `senior_citizen`, `partner`, `dependents`, `number_of_dependents`, `country`, `state`, `city`
- **Layanan yang Digunakan**: `internet_service`, `phone_service`, `multiple_lines`, `streaming_tv`, `streaming_movies`, `streaming_music`
- **Perilaku & Pengeluaran**: `tenure`, `monthly_charges`, `total_charges`, `payment_method`
- **Churn Info**: `churn_label`, `churn_value`, `churn_reason`
""")

# 4. Contoh Data
st.subheader("🔍 Contoh Data")
st.dataframe(df.sample(5, random_state=42))

# 5. Distribusi Churn
st.subheader("📊 Distribusi Churn")
churn_counts = df['churn_label'].value_counts().reset_index()
churn_counts.columns = ['Churn Label', 'Jumlah']

fig = px.pie(
    churn_counts,
    names='Churn Label',
    values='Jumlah',
    color='Churn Label',
    color_discrete_sequence=['#1f77b4', '#ff7f0e'],  # warna custom
    hole=0.3  # bikin jadi donut chart
)

fig.update_traces(
    textinfo='percent+label',
    pull=[0.05, 0],  # tarik sedikit slice churn
    textfont_size=14
)

fig.update_layout(
    showlegend=True,
    legend_title_text='Status Churn',
    plot_bgcolor='white'
)

st.plotly_chart(fig, use_container_width=True)

st.info("Dataset ini cukup kaya dengan **54 kolom** mencakup informasi demografi, layanan, perilaku, dan status churn.")

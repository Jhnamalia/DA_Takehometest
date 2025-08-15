import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Warna tema
churn_colors = px.colors.sequential.Magma

# ----------------------------
# Config dasar halaman
# ----------------------------
st.set_page_config(
    page_title="Business Recommendation",
    page_icon="💡",
    layout="wide"
)

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Normalisasi kolom kunci bila ada variasi penamaan
    # (Abaikan jika sudah konsisten)
    # Pastikan: churn_label (Yes/No), churn_value (0/1)
    if "churn_value" not in df.columns and "Churn Value" in df.columns:
        df = df.rename(columns={"Churn Value": "churn_value"})
    if "churn_label" not in df.columns and "Churn Label" in df.columns:
        df = df.rename(columns={"Churn Label": "churn_label"})
    return df

df = load_data("data/final_dataset.csv")
# Warna tema
churn_colors = px.colors.sequential.Magma

# ----------------------------
# Helper & Feature Engineering
# ----------------------------
def make_cltv_category(x):
    # Sesuaikan ambang jika mau
    if x < 2000:
        return "Low"
    elif x < 5000:
        return "Medium"
    else:
        return "High"

if "cltv" in df.columns:
    df["cltv_category"] = df["cltv"].apply(make_cltv_category)

# Tenure bin & Monthly charges bin untuk segmentasi
if "tenure" in df.columns:
    df["tenure_bin"] = pd.cut(
        df["tenure"],
        bins=[-1, 6, 12, 24, 48, df["tenure"].max()],
        labels=["≤6m", "7–12m", "13–24m", "25–48m", "49m+"]
    )

if "monthly_charges" in df.columns:
    df["charge_bin"] = pd.qcut(df["monthly_charges"], q=5, duplicates="drop")
    # qcut akan otomatis membagi menjadi kuantil

# ----------------------------
# Header & KPI
# ----------------------------
st.title("💡 Business Recommendation – Churn Reduction Playbook")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
total_customers = len(df)
churn_rate = df["churn_value"].mean() * 100 if "churn_value" in df.columns else np.nan
avg_tenure = df["tenure"].mean() if "tenure" in df.columns else np.nan
avg_arpu = df["monthly_charges"].mean() if "monthly_charges" in df.columns else np.nan

kpi1.metric("Total Pelanggan", f"{total_customers:,.0f}")
kpi2.metric("Churn Rate", f"{churn_rate:,.2f}%" if pd.notna(churn_rate) else "-")
kpi3.metric("Rata-rata Tenure (bulan)", f"{avg_tenure:,.1f}" if pd.notna(avg_tenure) else "-")
kpi4.metric("ARPU / Monthly Charges", f"{avg_arpu:,.0f}" if pd.notna(avg_arpu) else "-")

st.markdown("---")

# =========================
# Business Recommendations (Visual, Engaging)
# =========================
st.subheader("💡 Rekomendasi Bisnis – Churn Reduction Playbook")

# Gunakan Expander per kategori supaya rapi
with st.expander("1️⃣ Perkuat Loyalitas di Segmen Kritis", expanded=True):
    st.markdown(
        "📊 Prioritaskan program **loyalitas** dan **penawaran eksklusif** untuk segmen pelanggan yang menunjukkan potensi churn tinggi.\n\n"
        "🕒 Lakukan pemantauan tren bulanan untuk menangkap gejala awal penurunan retensi."
    )

with st.expander("2️⃣ Optimalkan Pendekatan Berdasarkan Profil Pelanggan"):
    st.markdown(
        "👶 Sesuaikan penawaran untuk kelompok usia muda dengan **paket fleksibel** dan **harga kompetitif.**\n\n"
        "🏙️ Bangun kampanye lokal yang relevan di wilayah dengan tingkat churn signifikan."
    )

with st.expander("3️⃣ Kembangkan Penawaran Layanan yang Lebih Menarik"):
    st.markdown(
        "📶 Tawarkan **upgrade paket** atau **bundling layanan** (Internet + TV + Phone) untuk meningkatkan nilai bagi pelanggan.\n\n"
        "📃 Dorong pelanggan kontrak bulanan untuk beralih ke kontrak tahunan dengan **insentif**."
    )

with st.expander("4️⃣ Fokus pada Pelanggan Bernilai Tinggi dan Baru"):
    st.markdown(
        "💰 Berikan perlakuan istimewa bagi pelanggan dengan CLTV tinggi melalui **program VIP.**\n\n"
        "⏱️ Untuk pelanggan tenure singkat, lakukan **onboarding & engagement awal** untuk meningkatkan loyalitas."
    )

with st.expander("5️⃣ Tingkatkan Kepuasan dan Respons Cepat"):
    st.markdown(
        "⭐ Follow-up cepat terhadap keluhan atau feedback negatif.\n\n"
        "🎁 Berikan reward atau bonus kecil untuk pelanggan yang puas dan aktif memberikan feedback."
    )

# Tambahkan sedikit styling sederhana supaya lebih menarik
st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
        font-size: 18px;
        font-weight: bold;
    }
    .streamlit-expanderContent {
        font-size: 16px;
        line-height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

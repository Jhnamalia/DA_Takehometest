import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🛠️ Data Preparation")
st.markdown("""
Tahap **Data Preparation** mencakup proses pembersihan data sebelum dilakukan analisis lebih lanjut.
""")

# Load dataset
df = pd.read_csv("data/final_dataset.csv")

# 1. Checking Missing Value
st.subheader("📌 Checking Missing Value")

st.markdown("#### 🧹 Riwayat Penanganan Missing Value")

st.markdown("""
Sebelum analisis, dataset ini memiliki beberapa kolom dengan missing value yang sudah ditangani sebagai berikut:

- **`offer`** (3877 missing) → Diisi dengan nilai **"No Offer"**.
- **`internet_type`** (1526 missing) → Diisi dengan nilai **"No Internet Service"**.
- **`churn_reason`** (5174 missing) → Diisi dengan nilai **"No Churn"**.

Metode ini digunakan untuk menjaga integritas data tanpa membuang baris yang masih relevan untuk analisis.
""")

missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]

if missing_values.empty:
    st.success("✅ Tidak ada missing value di dataset. Data sudah bersih!")
else:
    st.warning("⚠️ Terdapat missing value pada dataset:")
    st.dataframe(missing_values)

# 2. Checking Duplicated
st.subheader("📌 Checking Duplicated Data")
duplicates_count = df.duplicated().sum()
st.write(f"Jumlah data duplikat: **{duplicates_count}** (Tidak ditemukan duplikasi)")

# 3. Checking Outlier
st.subheader("📌 Checking Outlier (IQR Method)")

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

outlier_summary = {col: len(detect_outliers_iqr(df, col)) for col in numeric_cols}
outlier_df = pd.DataFrame(list(outlier_summary.items()), columns=["Kolom", "Jumlah Outlier"])
st.dataframe(outlier_df)

# Boxplot
st.subheader("📊 Visualisasi Outlier")
numerical_columns = [
    'age', 'number_of_dependents', 'tenure', 'avg_monthly_gb_download', 'number_of_referrals', 'monthly_charges',
    'avg_monthly_long_distance_charges', 'total_charges', 'total_refunds', 'total_extra_data_charges',
    'total_long_distance_charges', 'total_revenue', 'satisfaction_score', 'cltv', 'churn_score', 'churn_value',
    'zip_code', 'total_population', 'latitude', 'longitude', 'count', 'tenure_in_months'
]

fig, axes = plt.subplots(6, 4, figsize=(20, 18))
axes = axes.flatten()

for i, column in enumerate(numerical_columns):
    sns.boxplot(x=df[column], palette='Pastel1', ax=axes[i])
    axes[i].set_title(f"{column}", fontsize=10)

plt.tight_layout()
st.pyplot(fig)

# 4. Penjelasan
st.subheader("📍 Alasan Tidak Dilakukan Handling Outlier")
st.markdown("""
- **number_of_dependents** → Nilai tinggi realistis untuk keluarga besar.  
- **avg_monthly_gb_download** → Wajar untuk heavy internet users.  
- **number_of_referrals** → Bisa berasal dari influencer/reseller.  
- **total_refunds** → Kasus khusus kompensasi pelanggan.  
- **total_extra_data_charges** → Pelanggan sering melebihi kuota.  
- **total_long_distance_charges** → Wajar untuk pengguna bisnis atau lintas negara.  
- **total_revenue** → Pelanggan dengan multi-layanan.  
- **satisfaction_score** → Skor rendah/tinggi adalah feedback nyata.  
- **total_population** → Populasi tinggi wajar di kota besar.  
""")

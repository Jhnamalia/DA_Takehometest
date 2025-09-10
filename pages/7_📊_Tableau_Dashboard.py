import streamlit as st
from PIL import Image
import os

# ----------------------------
# Config halaman
# ----------------------------
st.set_page_config(
    page_title="📉 Tableau Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📉 Tableau Dashboards")
st.markdown("Berikut adalah beberapa dashboard Tableau yang digunakan dalam analisis Churn Pelanggan.")

# ----------------------------
# Path gambar
# ----------------------------
img_folder = "images"
dashboard_files = [
    "Dashboard_1.png",
    "Dashboard_2.png",
    "Dashboard_3.png",
    "Dashboard_4.png"
]

# Link Tableau Public (satu link untuk semua dashboard)
tableau_link = "https://public.tableau.com/shared/CNPHTQ4QX?:display_count=n&:origin=viz_share_link"

# ----------------------------
# Tampilkan dashboard
# ----------------------------
for i, file_name in enumerate(dashboard_files, start=1):
    img_path = os.path.join(img_folder, file_name)
    try:
        img = Image.open(img_path)
        st.subheader(f"📊 Dashboard {i}")
        st.image(img, use_container_width=True)
        st.markdown("---")
    except FileNotFoundError:
        st.error(f"❌ File {file_name} tidak ditemukan di folder {img_folder}.")

# ----------------------------
# Tambahkan link Tableau sekali di bawah
# ----------------------------
st.markdown(f"🔗 **Lihat versi interaktif di Tableau Public:** [Klik di sini]({tableau_link})")

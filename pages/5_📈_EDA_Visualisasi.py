import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/final_dataset.csv")

# Warna tema
churn_colors = px.colors.sequential.Magma

st.title("📊 Telco Customer Churn Dashboard")

# ====== Filter Interaktif ======
st.sidebar.header("🔍 Filter Data")
gender_filter = st.sidebar.multiselect(
    "Pilih Gender:",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Pilih Jenis Internet:",
    options=df["internet_type"].unique(),
    default=df["internet_type"].unique()
)

contract_filter = st.sidebar.multiselect(
    "Pilih Tipe Kontrak:",
    options=df["contract"].unique(),
    default=df["contract"].unique()
)

age_range = st.sidebar.slider(
    "Pilih Rentang Usia:",
    min_value=int(df["age"].min()),
    max_value=int(df["age"].max()),
    value=(int(df["age"].min()), int(df["age"].max()))
)

# Terapkan filter
df_filtered = df[
    (df["gender"].isin(gender_filter)) &
    (df["internet_type"].isin(internet_filter)) &
    (df["contract"].isin(contract_filter)) &
    (df["age"].between(age_range[0], age_range[1]))
]

# ====== Tab Layout ======
tab1, tab2, tab3 = st.tabs(["📈 Distribusi Umum", "💡 Layanan & Penggunaan", "⚠️ Faktor Churn"])

# ========================
# TAB 1 - DISTRIBUSI UMUM
# ========================
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        churn_counts = df_filtered['churn_label'].value_counts().reset_index()
        churn_counts.columns = ['Churn Label', 'Count']
        fig1 = px.pie(
            churn_counts,
            names="Churn Label",
            values="Count",
            title="Distribusi Status Pelanggan",
            color_discrete_sequence=churn_colors,
            hole=0.4
        )
        fig1.update_traces(textinfo='percent+label', textfont=dict(size=14))
       
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("📌 Mayoritas pelanggan berada pada status 'Tidak Churn', namun jumlah churn masih signifikan.")

    with col2:
        gender_counts = df_filtered.groupby(["gender", "churn_label"]).size().reset_index(name="Count")
        fig2 = px.bar(
            gender_counts,
            x="gender",
            y="Count",
            color="churn_label",
            title="Distribusi Gender & Status Pelanggan",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig2.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font

        st.plotly_chart(fig2, use_container_width=True)
        st.caption("📌 Tingkat churn relatif seimbang antara pelanggan pria dan wanita.")

    col3, col4 = st.columns(2)

    with col3:
        bins = [0, 29, 59, df_filtered["age"].max()]
        labels = ["<30", "30–59", "60+"]
        df_filtered["age_group"] = pd.cut(df_filtered["age"], bins=bins, labels=labels, right=True)
        age_counts = df_filtered.groupby(["age_group", "churn_label"]).size().reset_index(name="Count")
        fig3 = px.bar(
            age_counts,
            x="age_group",
            y="Count",
            color="churn_label",
            title="Distribusi Age Group",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig3.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font

        st.plotly_chart(fig3, use_container_width=True)
        st.caption("📌 Pelanggan usia 30–59 mendominasi basis pelanggan dan memiliki angka churn yang cukup tinggi.")

    with col4:
        top_10_city = df_filtered['city'].value_counts().head(10).reset_index()
        top_10_city.columns = ['City', 'Count']
        fig4 = px.bar(
            top_10_city, 
            x="Count",
            y="City",
            title="Top 10 Kota",
            orientation='h',
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig4.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font

        st.plotly_chart(fig4, use_container_width=True)
        st.caption("📌 Sebagian besar pelanggan berasal dari kota-kota besar, yang berpotensi menjadi target retensi utama.")

    st.subheader("📌 Distribusi Alasan Churn")
    churn_reason_counts = df_filtered[df_filtered['churn_label'] == 'Yes']['churn_reason'].value_counts().reset_index()
    churn_reason_counts.columns = ['Churn Reason', 'Count']
    fig_reason = px.bar(
        churn_reason_counts.head(10),
        x='Churn Reason',
        y='Count',
        title='Top 10 Alasan Pelanggan Churn',
        color='Count',
        color_continuous_scale=churn_colors,
        text="Count"  # label nilai
        )

    fig_reason.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font
    fig_reason.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_reason, use_container_width=True)
    st.caption("📌 Alasan utama pelanggan melakukan churn adalah kualitas layanan internet dan penawaran dari kompetitor lebih menarik, dan juga pelanggan merasa harga yang ditawarkan dianggap mahal dan tidak mendapatkan pelayanan yang memuaskan.")

# ========================
# TAB 2 - LAYANAN & PENGGUNAAN
# ========================
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        internet_counts = df_filtered.groupby(["internet_type", "churn_label"]).size().reset_index(name="Count")
        fig5 = px.bar(
            internet_counts,
            x="internet_type",
            y="Count",
            color="churn_label",
            title="Jenis Layanan Internet & Churn",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig5.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font
        st.plotly_chart(fig5, use_container_width=True)
        st.caption("📌 Tipe internet Fiber memiliki jumlah pelanggan terbesar namun juga memiliki churn yang cukup tinggi.")

    with col2:
        contract_counts = df_filtered.groupby(["contract", "churn_label"]).size().reset_index(name="Count")
        fig6 = px.bar(
            contract_counts,
            x="contract",
            y="Count",
            color="churn_label",
            title="Tipe Kontrak & Churn",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig6.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font
        st.plotly_chart(fig6, use_container_width=True)
        st.caption("📌 Pelanggan dengan kontrak bulanan memiliki tingkat churn paling tinggi dibanding kontrak tahunan.")

    col3, col4 = st.columns(2)

    with col3:
        fig7 = px.histogram(
            df_filtered,
            x="monthly_charges",
            color="churn_label",
            nbins=30,
            title="Distribusi Monthly Charges",
            color_discrete_sequence=churn_colors
        )
        st.plotly_chart(fig7, use_container_width=True)
        st.caption("📌 Pelanggan dengan biaya bulanan tinggi cenderung memiliki tingkat churn yang lebih besar.")

    with col4:
        fig8 = px.histogram(
            df_filtered,
            x="tenure",
            color="churn_label",
            nbins=30,
            title="Distribusi Tenure",
            color_discrete_sequence=churn_colors
        )
        st.plotly_chart(fig8, use_container_width=True)
        st.caption("📌 Pelanggan baru (tenure rendah) memiliki kecenderungan churn yang lebih tinggi.")
    
    # ========================
    # Skor Kepuasan Pelanggan
    # ========================
    st.subheader("⭐ Distribusi Skor Kepuasan Pelanggan")
    
    if "satisfaction_score" in df_filtered.columns:
        fig_satisfaction = px.histogram(
            df_filtered,
            x="satisfaction_score",
            color="churn_label",
            nbins=5,
            title="Skor Kepuasan Pelanggan & Status Churn",
            color_discrete_sequence=churn_colors
        )
        fig_satisfaction.update_layout(
            xaxis_title="Skor Kepuasan",
            yaxis_title="Jumlah Pelanggan"
        )
        st.plotly_chart(fig_satisfaction, use_container_width=True)
        st.caption("📌 Pelanggan dengan skor kepuasan ≤3 memiliki kemungkinan churn yang signifikan lebih tinggi dibandingkan pelanggan dengan skor 4 atau 5. Hal ini mengindikasikan bahwa tingkat kepuasan pelanggan merupakan indikator penting dalam memprediksi churn.")

# ========================
# TAB 3 - FAKTOR CHURN + Scatter + Maps
# ========================
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        payment_counts = df_filtered.groupby(["payment_method", "churn_label"]).size().reset_index(name="Count")
        fig9 = px.bar(
            payment_counts,
            x="payment_method",
            y="Count",
            color="churn_label",
            title="Metode Pembayaran & Churn",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig9.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font
        st.plotly_chart(fig9, use_container_width=True)
        st.caption("📌 Metode pembayaran otomatis memiliki churn yang lebih rendah dibanding pembayaran manual.")

    with col2:
        def cltv_category(cltv_value):
            if cltv_value < 2000:
                return "Low"
            elif cltv_value < 5000:
                return "Medium"
            else:
                return "High"
        df_filtered["cltv_category"] = df_filtered["cltv"].apply(cltv_category)
        cltv_counts = df_filtered.groupby(["cltv_category", "churn_label"]).size().reset_index(name="Count")
        fig_cltv = px.bar(
            cltv_counts,
            x="cltv_category",
            y="Count",
            color="churn_label",
            title="Customer Lifetime Value (CLTV) vs Churn",
            barmode="group",
            color_discrete_sequence=churn_colors,
            text="Count"  # label nilai
        )

        fig_cltv.update_traces(textposition='outside', textfont=dict(size=12))  # posisi & ukuran font
        st.plotly_chart(fig_cltv, use_container_width=True)
        st.caption("📌 Pelanggan dengan CLTV medium memiliki risiko churn yang lebih tinggi, dibandingkan pelanggan dengan CLTV tinggi.")

    tenure_churn = df_filtered.groupby("tenure")["churn_value"].mean().reset_index()
    tenure_churn["Churn Rate (%)"] = tenure_churn["churn_value"] * 100
    fig11 = px.line(
        tenure_churn,
        x="tenure",
        y="Churn Rate (%)",
        markers=True,
        title="Churn Rate Berdasarkan Tenure",
        color_discrete_sequence=["#d62728"]
    )
    st.plotly_chart(fig11, use_container_width=True)
    st.caption("📌 Churn rate menurun seiring bertambahnya masa berlangganan pelanggan.")

    # Scatter Plot
    st.subheader("📈 Hubungan Biaya Bulanan & CLTV")
    fig_scatter = px.scatter(
        df_filtered,
        x="monthly_charges",
        y="cltv",
        color="churn_label",
        title="Monthly Charges vs CLTV",
        size="tenure",
        hover_data=["customer_id", "internet_type", "contract"],
        color_discrete_sequence=churn_colors
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.caption("📌 Pelanggan dengan biaya bulanan tinggi dan CLTV rendah cenderung churn lebih banyak.")

    # Maps
    st.subheader("🗺️ Peta Distribusi Pelanggan")
    fig_map = px.scatter_mapbox(
        df_filtered,
        lat="latitude",
        lon="longitude",
        color="churn_label",
        hover_name="city",
        hover_data=["state", "internet_type", "contract"],
        zoom=4,
        height=500,
        color_discrete_sequence=churn_colors
    )
    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map, use_container_width=True)
    st.caption("📌 Sebaran pelanggan di seluruh wilayah, ukuran titik menunjukkan besarnya biaya bulanan.")

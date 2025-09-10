import streamlit as st
from PIL import Image

# Judul halaman
st.title("👤 About Me")

# Layout kolom untuk foto dan deskripsi
col1, col2 = st.columns([1, 3])

with col1:
    image = Image.open("images/jihan_amalia.jpg")
    st.image(image, caption="Jihan Amalia", use_container_width=True)

with col2:
    st.markdown("""
    ### Halo! 👋 Saya Jihan Amalia
    Saya adalah seorang **Data Analyst** yang memiliki ketertarikan di bidang **Data Analyst, Data Science, Business Intelligence, dan Machine Learning**.  
    Saya senang mengolah data menjadi insight yang bermanfaat dan membantu pengambilan keputusan berbasis data.

    Saat ini, saya telah **menyelesaikan proyek analisis churn pelanggan (customer churn)** menggunakan dataset *Telco Customer Churn* dari Kaggle.  
    Proyek ini mencakup **Business Understanding, Data Understanding, Data Preparation, Exploratory Data Analysis (EDA), hingga Business Recommendation**, yang divisualisasikan melalui **Streamlit Dashboard** dan **Tableau**.

    **🔍 Keahlian Utama:**
    - Data Cleaning & Preprocessing  
    - Exploratory Data Analysis (EDA)  
    - Data Visualization (Matplotlib, Plotly, Tableau, Power BI)  
    - Machine Learning (Supervised & Unsupervised)  
    - Dashboard Development (Streamlit, Tableau, Power BI)  

    **🎓 Pendidikan:**  
    - Full-Stack Data Analyst & Data Science Bootcamp – [Dibimbing.id]  
    - Budidaya Perairan - [Universitas Jenderal Soedirman]  

    **💡 Motto:**  
    > “Committed to use my technical and analytical skills to provide valuable insights and data-driven solutions and adapt quickly to industry changes”
    """)

st.markdown("---")
st.subheader("🔗 Project Resources")
st.markdown("""
- 📄 **Project Slide Deck**: [Stop the Churn: Telco Customer Insights & Strategy](https://drive.google.com/file/d/1_fu-mzGYZwPan4bUz-3l4IVfVcg5SEWY/view?usp=drive_link)  
- 📊 **Dataset Source**: [Why Do Customers Leave? Telco Customer Churn Dataset - Kaggle](https://www.kaggle.com/datasets/hassanelfattmi/why-do-customers-leave-can-you-spot-the-churners?select=a_IBM+Telco+Customers+Churn+Datasets.xlsx)  
- 📈 **Tableau Dashboard**: [Customer Insights & Business Performance Dashboard](hhttps://public.tableau.com/shared/CNPHTQ4QX?:display_count=n&:origin=viz_share_link)  
""")

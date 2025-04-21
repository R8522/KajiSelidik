import streamlit as st

# App Title
st.set_page_config(page_title="Analisis Perpustakaan Perpustakaan Desa/Komuniti", layout="centered")
st.title("📚 Sistem Analisis Perpustakaan Desa/Komuniti")

# Sidebar Navigation
st.sidebar.header("📂 Pilih Lokasi")
page = st.sidebar.selectbox(
    "Lokasi Komuniti:",
    ["Desa Sempeneh", "Kuala Dipang"]
)

# Routing
if page == "Desa Sempeneh":
    import DesaSempeneh
    DesaSempeneh.run()

elif page == "Kuala Dipang":
    import KualaDipang
    KualaDipang.run()

# Optional footer
st.markdown("---")
st.caption("Dibangunkan oleh 🧠 Sistem Analitik Komuniti | Projek Latihan Industri")

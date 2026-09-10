import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title(":calendar: Analisis Waktu")
st.write("Halaman ini menampilkan pola jumlah hotspot berdasarkan bulan serta perbandingan deteksi pada siang dan malam hari.")

bulanan = (df.groupby(df["acq_date"].dt.month).size().reset_index(name="Jumlah"))

bulanan["Bulan"] = bulanan["acq_date"].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"Mei", 6:"Jun", 7:"Jul", 8:"Agu", 9:"Sep", 10:"Okt", 11:"Nov", 12:"Des"})

st.subheader("Hotspot per Bulan")

fig = px.line(bulanan, x="Bulan", y="Jumlah", markers=True)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Hotspot Siang dan Malam")

waktu = df["waktu"].value_counts().reset_index()
waktu.columns = ["Waktu", "Jumlah"]

fig2 = px.pie(waktu, names="Waktu", values="Jumlah")

st.plotly_chart(fig2, use_container_width=True)
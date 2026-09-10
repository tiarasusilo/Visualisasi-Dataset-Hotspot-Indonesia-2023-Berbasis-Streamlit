import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title(":fire: Dashboard Hotspot Indonesia 2023")

st.write("Dashboard ini menampilkan informasi hotspot di Indonesia tahun 2023, meliputi jumlah hotspot, tingkat confidence, dan nilai FRP.")

c1, c2, c3 = st.columns(3)
c1.metric("Total Hotspot", len(df))
c2.metric("Rata-rata Confidence", f"{df['confidence'].mean():.1f}%")
c3.metric("Rata-rata FRP", f"{df['frp'].mean():.1f} MW")

bulan = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"Mei", 6:"Jun", 7:"Jul", 8:"Agu", 9:"Sep", 10:"Okt", 11:"Nov", 12:"Des"}

bulanan = (df.groupby(df["acq_date"].dt.month)
    .agg(Jumlah=("latitude", "count"), Confidence=("confidence", "mean"), FRP=("frp", "mean"))
    .reset_index()
)

bulanan["Bulan"] = bulanan["acq_date"].map(bulan)

st.subheader("Hotspot per Bulan")

fig = px.bar(bulanan, x="Bulan", y="Jumlah")
st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Tampilkan Tabel Data per Bulan"):
    st.write("Berikut ringkasan data hotspot berdasarkan bulan selama tahun 2023.")

    st.dataframe(bulanan[["Bulan", "Jumlah", "Confidence", "FRP"]], use_container_width=True, hide_index=True)
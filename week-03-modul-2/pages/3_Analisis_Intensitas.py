import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title(":zap: Analisis Intensitas")
st.write("Halaman ini menampilkan tingkat intensitas hotspot berdasarkan nilai FRP serta data hotspot dengan nilai FRP tertinggi.")

c1, c2 = st.columns(2)

c1.metric("Rata-rata FRP", f"{df['frp'].mean():.1f} MW")
c2.metric("FRP Tertinggi", f"{df['frp'].max():.1f} MW")

st.subheader("Distribusi FRP")

fig = px.histogram(df[df["frp"] < 150], x="frp", nbins=30)

st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Tampilkan 10 Data FRP Tertinggi"):
    st.dataframe(
        df.nlargest(10, "frp")[
            ["acq_date", "latitude", "longitude", "confidence", "frp"]
        ],
        use_container_width=True,
        hide_index=True
    )
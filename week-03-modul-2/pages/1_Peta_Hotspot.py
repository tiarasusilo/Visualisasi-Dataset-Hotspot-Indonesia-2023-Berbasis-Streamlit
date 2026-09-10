import streamlit as st
from utils import load_data

df = load_data()

st.title(":world_map: Peta Hotspot")
st.write("Halaman ini menampilkan persebaran lokasi hotspot di Indonesia berdasarkan koordinat latitude dan longitude.")

confidence = st.slider("Confidence", 0, 100, (0, 100))

filter_df = df[df["confidence"].between(confidence[0], confidence[1])]

st.metric("Jumlah Hotspot", len(filter_df))

if len(filter_df) > 0:
    st.map(filter_df[["latitude", "longitude"]].sample(
            min(10000, len(filter_df)),
            random_state=42
        )
    )
else:
    st.warning("Tidak ada data hotspot pada confidence tersebut.")
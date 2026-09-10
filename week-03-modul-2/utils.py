import streamlit as st
import pandas as pd

URL = "https://raw.githubusercontent.com/apkirana/project_forestfire/main/assets/data/indonesia2023.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(URL, dtype={"acq_time": str})

    df["acq_date"] = pd.to_datetime(df["acq_date"])
    df["acq_time"] = df["acq_time"].str.zfill(4)

    df = df.dropna(subset=["latitude", "longitude", "acq_date"])

    df["bulan"] = df["acq_date"].dt.month_name()
    df["waktu"] = df["daynight"].map({"D": "Siang", "N": "Malam"})

    return df
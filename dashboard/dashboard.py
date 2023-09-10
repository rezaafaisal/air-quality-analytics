import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_yearly_vehicle_df(df):
    yearly_vehicle_df = df.resample(rule='Y', on='datetime').agg({
        "vehicle_pollution": "mean"
    })
    
    yearly_vehicle_df = yearly_vehicle_df.reset_index()
    yearly_vehicle_df.rename(columns={
        "vehicle_pollution": "vehicle_pollution_average"
    })
    
    return yearly_vehicle_df

# load dataframe
all_data = pd.read_csv('all_data.csv')
all_data['datetime'] = pd.to_datetime(all_data['datetime'])

min_date = all_data.datetime.min()
max_date = all_data.datetime.max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_data[(all_data['datetime'] >= str(start_date)) & (all_data['datetime'] <= str(min_date))]
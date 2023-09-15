import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import source as src # data source 

data = src.all_data

# style
st.markdown("""
        <style>
            .title{
                font-size: 25px !important;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)


# header
col_1, col_2 = st.columns(2)
with col_1:
    st.markdown("<span class='title'>AIR QUALITY DAHBOARD</span>", unsafe_allow_html=True)
    st.write("###")
    
col_2_1, col_2_2 = col_2.columns(2)
with col_2_1:
    stations = src.get_station(data)
    station = st.selectbox(label="Station", label_visibility='collapsed', options=stations)
    st.write("###")
    
with col_2_2:
    years = src.get_year(data)
    year = st.selectbox(label="Pollutan", label_visibility='collapsed', options=years)
    
bar_1, bar_2, bar_3, bar_4 = st.columns(4)
with bar_1:
    industry_pollutan = src.get_average_industry_by_year(data, year, station).values[0]
    st.metric("Industry Pollution", value=industry_pollutan)
with bar_2:
    vehicle_pollutan = src.get_average_vehicle_by_year(data, year, station).values[0]
    st.metric("Vehicle Pollution", value=vehicle_pollutan)
with bar_3:
    temp = src.dashboard_bar(data, year, station).temp
    st.metric("Temperature", value=f"{temp} °C")
with bar_4:
    wind = src.dashboard_bar(data, year, station).wind
    st.metric("Wind", value=f"{wind} MPh")
    
# rata-rata polusi kendaraan
with st.container():
    st.write("#")
    vehicle_pollutan = src.get_average_vehicle_by_year(data, year, station)
    fig = px.line(vehicle_pollutan, title="Average Vehicle Pollution by Month", labels={"index":"Month", "value":"Average Pollution"})
    fig.update_traces(showlegend=False, mode="lines+markers")
    st.write(fig)
    
# rata-rata polusi industri
with st.container():
    st.write("#")
    industry_pollutan = src.get_average_industry_by_year(data, year, station)
    fig = px.line(industry_pollutan, title="Average Industrial Pollution by Month", labels={'index': 'Month', 'value':'Average Pollution'})
    fig.update_traces(showlegend=False, mode="lines+markers")
    st.write(fig)

with st.container():
    pollutan = src.pollutan_by_year(data, station, year)
    
    fig = px.bar(pollutan,
                 orientation='h',
                 title="Average Pollution Particles",
                 labels={"index": "Particle", "value":"Amount"},
                 color=pollutan.index,
                 color_discrete_sequence=["#ef4444", "#f87171", "#94a3b8", "#94a3b8", "#94a3b8", "#94a3b8"])
    fig.update_traces(showlegend=False)
    st.write(fig)
    

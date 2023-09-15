import streamlit as st
import numpy as np
import plotly.express as px
import source as src

data = src.all_data

st.markdown("""
        <style>
            .title{
                font-size: 25px !important;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

st.markdown("<span class='title'>YEARLY AIR QUALITY DAHBOARD</span>", unsafe_allow_html=True)
st.write("###")

col_1, col_2 = st.columns(2)

with col_1:
    stations = src.get_station(data)
    station = st.selectbox('Station', options=stations)

with col_2:
    years = src.get_year(data)
    year = st.selectbox('Year', options=years)
    

with st.container():
    st.write("###")
    temp, rain, wind = src.yearly_bar(data, station, year)
    bar_1, bar_2, bar_3 = st.columns(3)
    with bar_1:
        st.metric("Temperature (Avg)", f"{temp} °C")
    with bar_2:
        st.metric("Rain (Avg)", f"{rain}")
    with bar_3:
        st.metric("Wind (Avg)", f"{wind} MPh")

with st.container():
    st.write("#")
    yearly_pollutan = src.yearly_pollution(data, station, year)
    fig = px.line(yearly_pollutan,
                  title="Average Pollution Particles by Month",
                  labels={"index":"Month", "value":"Amount", "variable":"Particles"})
    
    fig.update_traces(showlegend=True, mode="lines+markers")
    st.write(fig)
    


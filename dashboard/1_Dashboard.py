import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
    st.selectbox(label="Station", label_visibility='collapsed', options=['asas', 'asas', 'asas'])
    st.write("###")
    
with col_2_2:
    st.selectbox(label="Pollutan", label_visibility='collapsed', options=['asas', 'asasa'])
    
bar_1, bar_2, bar_3, bar_4 = st.columns(4)
with bar_1:
    st.metric("Industry Pollution", value=3434)
with bar_2:
    st.metric("Vehicle Pollution", value=3434)
with bar_3:
    st.metric("Temperature", value=3434)
with bar_4:
    st.metric("Air Pressure", value=3434)
    
# rata-rata polusi kendaraan dan industri
with st.container():
    st.write("#")
    st.caption("Average Pullution")
    st.line_chart(np.random.randn(12, 2))

with st.container():
    st.caption("Total Jumlah Polusi")
    df = pd.DataFrame(
    np.random.randn(5, 7),
    columns=['Station', 'PM2.5','PM10', 'SO2', 'NO2', 'CO', 'O3']).set_index('Station')
    st.table(df)
    

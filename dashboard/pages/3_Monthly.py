import streamlit as st
import numpy as np

st.subheader('Monthly Air Quality')

col_1, col_2, col_3, col_4 = st.columns(4)

with col_1:
    st.selectbox('Station', options=['Pertama', 'kedua', 'ketiga'])
with col_2:
    st.selectbox('Pollutan', options=['Pertama', 'kedua', 'ketiga'])
with col_3:
    st.selectbox('Year', options=['Pertama', 'kedua', 'ketiga'])
with col_4:
    st.selectbox('Month', options=['Pertama', 'kedua', 'ketiga'])

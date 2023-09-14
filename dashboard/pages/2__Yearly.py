import streamlit as st
import numpy as np

st.subheader('Yearly Air Quality')

col_1, col_2, col_3 = st.columns(3)

with col_1:
    st.selectbox('Station', options=['Pertama', 'kedua', 'ketiga'])

with col_2:
    st.selectbox('Pollutan', options=['2018', '2019', '2020'])
    
with col_3:
    st.selectbox('Year', options=['2018', '2019', '2020'])
    
with st.container():
    st.write('aowkoakw')
    st.bar_chart(np.random.randn(50, 3))
    
with st.container():
    st.bar_chart(np.random.randn(50,4))


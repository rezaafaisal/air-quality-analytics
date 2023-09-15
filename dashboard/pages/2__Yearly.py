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
    st.write("###")
    bar_1, bar_2, bar_3 = st.columns(3)
    with bar_1:
        st.metric("Temperature", "45 F", "-12 F")
    with bar_2:
        st.metric("Rain", "45 F")
    with bar_3:
        st.metric("Wind", "45 F")

with st.container():
    st.write("#")
    st.write('aowkoakw')
    st.bar_chart(np.random.randn(50, 3))
    


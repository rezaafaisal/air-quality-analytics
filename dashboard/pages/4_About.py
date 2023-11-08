import streamlit as st

st.write("<div style='text-align: center;font-size: 25px;font-weight: bold;margin-bottom:50px;'>About Me</div>", unsafe_allow_html=True)

col_1, col_2 = st.columns([1,2])
with col_1:
    st.write("<div style=''><img style='border-radius:50%' src='https://raw.githubusercontent.com/rezaafaisal/source/images/photo/cat.jpeg' width='200px' height='200px' /></div>", unsafe_allow_html=True)

with col_2:
    st.text("Nama : Reza Faisal")
    st.text("Email : rezha.faizal567@gmail.com")
    st.text("Dicoding Username : rezaafaisal")
    st.write("""
             <div>
                <a href='https://instagram.com/rezaa.faisal' style='margin-right:5px;' target='_blank'>
                    <img src='https://raw.githubusercontent.com/rezaafaisal/source/images/icon/instagram.png' height='20px' width='20px'>
                </a>
                <a href='https://linkedin.com/in/rezafaisal' target='_blank'>
                    <img src='https://raw.githubusercontent.com/rezaafaisal/source/images/icon/linkedin.png' height='20px' width='20px'>
                </a>
             </div>
             
             """, unsafe_allow_html=True)

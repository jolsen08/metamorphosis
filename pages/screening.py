import streamlit as st

st.set_page_config(
    page_title='Metamorphosis | Screening',
     layout='wide'
)

col1, col2 = st.columns(2)
with col1:
    st.title("Welcome to Mental Health Screening")
with col2:
    st.subheader("Please fill out the following quesionnaires to set up your account.")

st.subheader("Your Mental Health Score: 3.9")
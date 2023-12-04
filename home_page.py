import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Metamorphosis',
    layout='wide'
)

# Initialize session state
if 'cookie_agreement' not in st.session_state:
    st.session_state['cookie_agreement'] = False

# Placeholder for main content
main_content = st.empty()

if st.session_state['cookie_agreement']:
    # Display the main content of the page
    with main_content.container():
        st.title("Welcome to Missionary Mental Health - Metamorphosis. This is the Home Page")
        # Add the rest of your Streamlit components here
else:
    # Overlay the cookie policy agreement
    with main_content.container():
        st.title("Cookie Policy Agreement")
        st.write("We use cookies to improve your experience on our site. Please agree to our cookie policy to continue.")
        if st.button("I agree to the cookie policy"):
            st.session_state['cookie_agreement'] = True
            st.experimental_rerun()

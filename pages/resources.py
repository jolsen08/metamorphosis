import streamlit as st
import base64
import smtplib
from home_page import append_to_file

st.set_page_config(
    page_title='Metamorphosis | Resources',
    layout='wide'
)

st.title("Welcome to Resources")

form_space = st.empty()

with form_space.form("Stress Level"):
    if 'stress_level' not in st.session_state:
        stress_level = st.selectbox("Please select a Stress Level",[1,2,3,4,5])
        submit = st.form_submit_button("Next")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - Stress Level Submission at"
            append_to_file(text_to_append)
            if stress_level < 4:
                st.session_state.suicide_question = 'No'
            st.session_state.stress_level = stress_level
            st.rerun()
    elif st.session_state.stress_level > 3 and 'suicide_question' not in st.session_state:
        suicide_question = st.selectbox("Are you struggling with suicidal thoughts or other thoughts that require immediate attention?",['Yes','No'])
        submit = st.form_submit_button("Next")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - suicide question at"
            append_to_file(text_to_append)
            st.session_state.suicide_question = suicide_question
            st.rerun()
    elif st.session_state.suicide_question == 'Yes':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = 'metamissionary.health@gmail.com'
        server.login(sender_email, 'qaia vwbf dpku sgbx')
        receiver_email = 'president.lebron.james@gmail.com'
        message = f'''Subject: Missionary Mental Health Alert

Dear President James,

Elder James Butler recently reported high stress levels and indicated suicidal thoughts or urgent attention. His email is james.butler@missionary.org and he is currently serving in the Blue Lagoon Ward in the Miami Florida Stake.

Thank you,
MetaMissionary Health
'''
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        st.subheader("Your Mission President has been alerted. Please call or text 988 (the suicide hotline)!")
        submit = st.form_submit_button("OK")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - OK button if clicked yes for suicidal thoughts at"
            append_to_file(text_to_append)
            session_state = st.session_state
            for key in list(session_state.keys()):
                del session_state[key]
            st.rerun()

    elif 'stress_causer' not in st.session_state:
        stress_causer = st.multiselect("Where is most of your stress coming from?",['Physical Demands','Emotional Demands','Social Demands','Intellectual Demands','Spiritual Demands'])
        submit = st.form_submit_button("Next")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - Where stress is coming from button at"
            append_to_file(text_to_append)
            st.session_state.stress_causer = stress_causer
            st.rerun()
    else:
        expansion = True
        if len(st.session_state.stress_causer) > 1:
            expansion = False
        if 'Physical Demands' in st.session_state.stress_causer:
            with st.expander("Physical Demands Resources", expanded=expansion):
                pdf_path = "pages/pdfs/physical.pdf"
                st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_path, "rb").read()).decode()}" width="700" height="800" style="border:none;"></iframe>', unsafe_allow_html=True)

        if 'Emotional Demands' in st.session_state.stress_causer:
            with st.expander("Emotional Demands Resources", expanded=expansion):
                pdf_path = "pages/pdfs/emotional.pdf"
                st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_path, "rb").read()).decode()}" width="700" height="800" style="border:none;"></iframe>', unsafe_allow_html=True)
        
        if 'Social Demands' in st.session_state.stress_causer:
            with st.expander("Social Demands Resources", expanded=expansion):
                pdf_path = "pages/pdfs/social.pdf"
                st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_path, "rb").read()).decode()}" width="700" height="800" style="border:none;"></iframe>', unsafe_allow_html=True)

        if 'Intellectual Demands' in st.session_state.stress_causer:
            with st.expander("Intellectual Demands Resources", expanded=expansion):
                pdf_path = "pages/pdfs/intellectual.pdf"
                st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_path, "rb").read()).decode()}" width="700" height="800" style="border:none;"></iframe>', unsafe_allow_html=True)

        if 'Spiritual Demands' in st.session_state.stress_causer:
            with st.expander("Spiritual Demands Resources", expanded=expansion):
                pdf_path = "pages/pdfs/spiritual.pdf"
                st.markdown(f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_path, "rb").read()).decode()}" width="700" height="800" style="border:none;"></iframe>', unsafe_allow_html=True)

        submit = st.form_submit_button("Start Over")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - Start Over"
            append_to_file(text_to_append)
            session_state = st.session_state
            for key in list(session_state.keys()):
                del session_state[key]

            st.rerun()

import streamlit as st
import base64
import smtplib
# from home_page import append_to_file

st.set_page_config(
    page_title='Metamorphosis | Resources',
    layout='wide',
    page_icon='data:image/png;base64,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'
)

st.title("Welcome to Resources")

form_space = st.empty()

with form_space.form("Stress Level"):
    if 'stress_level' not in st.session_state:
        if 'user_scores' not in st.session_state:
            stress_level = st.selectbox("Please select a Stress Level",[1,2,3,4,5])
        else:
            score_df = st.session_state.user_scores
            last_row = score_df.iloc[-1].to_dict()
            st.write(f"Your mental health score is {last_row['Total_Score']} based on your last screening submission, submitted on {last_row['Date']}")
            if last_row['Total_Score'] <= 9.6:
                stress_level = 1
            elif last_row['Total_Score'] <= 19.2:
                stress_level = 2
            elif last_row['Total_Score'] <= 28.8:
                stress_level = 3
            elif last_row['Total_Score'] <= 38.4:
                stress_level = 4
            else:
                stress_level = 5
        submit = st.form_submit_button("Next")
        if submit:
            #append to text file upon click
            text_to_append = "Resources - Stress Level Submission at"
            # append_to_file(text_to_append)
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
            # append_to_file(text_to_append)
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
            # append_to_file(text_to_append)
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
            # append_to_file(text_to_append)
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
            # append_to_file(text_to_append)
            session_state = st.session_state
            for key in list(session_state.keys()):
                if key != 'user_scores':
                    del session_state[key]

            st.rerun()

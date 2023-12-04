import streamlit as st
import base64


st.set_page_config(
    page_title='Metamorphosis | Resources',
    layout='wide'
)

st.title("Welcome to Resources")

<<<<<<< HEAD
form_space = st.empty()

with form_space.form("Stress Level"):
    if 'stress_level' not in st.session_state:
        stress_level = st.selectbox("Please select a Stress Level",[1,2,3,4,5])
        submit = st.form_submit_button("Next")
        if submit:
            if stress_level < 4:
                st.session_state.suicide_question = 'No'
            st.session_state.stress_level = stress_level
            st.rerun()
    elif st.session_state.stress_level > 3 and 'suicide_question' not in st.session_state:
        suicide_question = st.selectbox("Are you struggling with suicidal thoughts or other thoughts that require immediate attention?",['Yes','No'])
        submit = st.form_submit_button("Next")
        if submit:
            st.session_state.suicide_question = suicide_question
            st.rerun()
    elif st.session_state.suicide_question == 'Yes':
        st.subheader("Please call or text 988 (the suicide hotline)!")
        submit = st.form_submit_button("OK")
        if submit:
            session_state = st.session_state
            for key in list(session_state.keys()):
                del session_state[key]
            st.rerun()

    elif 'stress_causer' not in st.session_state:
        stress_causer = st.multiselect("Where is most of your stress coming from?",['Physical Demands','Emotional Demands','Social Demands','Intellectual Demands','Spiritual Demands'])
        submit = st.form_submit_button("Next")
        if submit:
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
            session_state = st.session_state
            for key in list(session_state.keys()):
                del session_state[key]

            st.rerun()
=======
# Define your resources
resources = {
    "Loneliness": [
        {"text": "Luke 6:21-22", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/luke/6?lang=eng#p35"},
        {"text": "John 16:32-33", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/16?lang=eng#title_number1"}
    ],
    "Depression or Anxiety": [
        {"text": "Fear Not: Believe Only! - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2022/04/23holland?lang=eng#title1"},
        {"text": "Addressing Mental Health - Elder Erich W. Kopischke", "url": 'https://www.churchofjesuschrist.org/study/general-conference/2021/10/25kopischke?lang=eng#title1'},
        {"text": "Behold the Man - Elder Dieter F. Uchtdorf", "url": "https://www.churchofjesuschrist.org/study/general-conference/2018/04/behold-the-man?lang=eng#title1"}
    ],
    "Peace": [
        {"text": "John 14:26-27", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/14?lang=eng#title_number1"}, 
        {"text": "John 14:18", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/14?lang=eng#title_number1"},
        {"text": "Jacob 3:1", "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/jacob/3?lang=eng#study_summary1"}
    ],
    "Imperfection": [
        {"text": "Charity Never Faileth - President Thomas S. Monson", "url": "https://www.churchofjesuschrist.org/study/general-conference/2010/10/charity-never-faileth?lang=eng#p42"},
        {"text": "The Laborers in the Vineyard - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2012/04/the-laborers-in-the-vineyard?lang=eng"},
        {"text": "Worthiness is Not Flawlessness - Brad R. Wilcox", "url": "https://www.churchofjesuschrist.org/study/general-conference/2021/10/35wilcox?lang=eng"},
        {"text": "Be Ye Therefore Perfect – Eventually - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2017/10/be-ye-therefore-perfect-eventually?lang=eng"}
    ],
    "Self-Worth": [
        {"text": "This Is Our Time! - Elder S. Gifford Nielsen", "url": "https://www.churchofjesuschrist.org/study/general-conference/2021/04/33nielsen?lang=eng"},
        {"text": "Eyes to See - Michelle D. Craig", "url": "https://www.churchofjesuschrist.org/study/general-conference/2020/10/14craig?lang=eng"},
        {"text": "Of Things That Matter Most - President Dieter F. Uchtdorf", "url": "https://www.churchofjesuschrist.org/study/general-conference/2010/10/of-things-that-matter-most?lang=eng"},
        {"text": "To Young Women - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2005/10/to-young-women?lang=eng"},
        {"text": "The Other Prodigal - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2002/04/the-other-prodigal?lang=eng"},
        {"text": "Value beyond Measure - Joy D. Jones", "url": "https://www.churchofjesuschrist.org/study/general-conference/2017/10/value-beyond-measure?lang=eng"},
        {"text": "1 Corinthians 3:23", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/1-cor/3?lang=eng"},
        {"text": "1 Corinthians 3:16-20", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/1-cor/3?lang=eng"},
        {"text": "Psalm 82:6", "url": "https://www.churchofjesuschrist.org/study/scriptures/ot/ps/82?lang=eng"},
        {"text": "Deuteronomy 7:6-9", "url": "https://www.churchofjesuschrist.org/study/scriptures/ot/deut/7?lang=eng"}
    ],
    "Overcoming Trials": [
        {"text": "Try, Try, Try - President Henry B. Eyring", "url": "https://www.churchofjesuschrist.org/study/general-conference/2018/10/try-try-try?lang=eng"},
        {"text": "The Power of Spiritual Momentum - President Russell M. Nelson", "url": "https://www.churchofjesuschrist.org/study/general-conference/2022/04/47nelson?lang=eng"},
        {"text": "Highly Favored of the Lord - Elder Gary E. Stevenson", "url": "https://www.churchofjesuschrist.org/study/general-conference/2020/10/53stevenson?lang=eng"},
        {"text": "As Many as I Love, I Rebuke and Chasten - Elder D. Todd Christofferson", "url": "https://www.churchofjesuschrist.org/study/general-conference/2011/04/as-many-as-i-love-i-rebuke-and-chasten?lang=eng"},
        {"text": "Waiting on the Lord - Elder Jeffrey R. Holland", "url": "https://www.churchofjesuschrist.org/study/general-conference/2020/10/57holland?lang=eng"},
        {"text": "Christ Is Risen; Faith in Him Will Move Mountains - President Russell M. Nelson", "url": "https://www.churchofjesuschrist.org/study/general-conference/2021/04/49nelson?lang=eng"},
        {"text": "Our Sorrow Shall Be Turned into Joy - Elder S. Mark Palmer", "url": "https://www.churchofjesuschrist.org/study/general-conference/2021/04/43palmer?lang=eng"},
        {"text": "Doctrine and Covenants 24:8", "url": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/24?lang=eng"},
        {"text": "Doctrine and Covenants 78:18", "url": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/78?lang=eng"},
        {"text": "Jacob 3:1", "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/jacob/3?lang=eng"},
        {"text": "2 Corinthians 4:17-18", "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/2-cor/4?lang=eng"}
    ]
}

# Display headers and links
for category, verses in resources.items():
    st.header(category)
    for verse in verses:
        st.markdown(f"[{verse['text']}]({verse['url']})")
>>>>>>> 3a8dda90409a9ea31cb739198e18ac833c663ceb

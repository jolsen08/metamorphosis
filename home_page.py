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
        # Create a form for ranking categories
        st.subheader("Over the last 2 weeks, how often have you been bothered by any of the following problems?")

        # Define categories
        categories = ["Little interest or pleasure in doing things", "Feeling down, depressed or hopeless", "Trouble falling or staying asleep, or sleeping too much", "Feeling tired or having little energy", "Poor appetite or overeating", "Feeling bad about yourself - or that you are a failure or have let yourself or your family down", "Trouble concentrating on things, such as reading the newspaper or watching television", "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", "Thoughts that you would be better off dead, or of hurting yourself in some way", "Feeling nervous, anxious or on edge", "Not being able to stop or control worrying", "Worrying too much about different things", "Trouble relaxing", "Being so restless that it is hard to sit still", "Becoming easily annoyed or irritable", "Feeling afraid, as if something awful might happen"]

        # Create a dictionary to store user rankings
        user_rankings = {}

        ranking_options = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

        # Create a form for ranking
        for category in categories:
            user_rankings[category] = st.radio(f"{category}", options=ranking_options)

        # Submit button
        if st.button("Submit Rankings"):
            # Display user rankings
            st.success("Rankings Submitted!")
            st.write("User Rankings:")
            for category, ranking in user_rankings.items():
                st.write(f"{category}: {ranking}")
            
            # You can save the rankings to a file or database if needed
            # For example, save to a CSV file
            rankings_df = pd.DataFrame(list(user_rankings.items()), columns=['Category', 'Ranking'])
            rankings_df.to_csv('user_rankings.csv', index=False)
else:
    # Overlay the cookie policy agreement
    with main_content.container():
        st.title("Cookie Policy Agreement")
        st.write("We use cookies to improve your experience on our site. Please agree to our cookie policy to continue.")
        if st.button("I agree to the cookie policy"):
            st.session_state['cookie_agreement'] = True
            st.experimental_rerun()

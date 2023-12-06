import pandas as pd
import streamlit as st
import altair as alt
from datetime import datetime


st.set_page_config(
    page_title='Metamorphosis',
    layout='wide'
)

def append_to_file(text_to_append):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Combine timestamp and text
    entry = f"{text_to_append} {timestamp}\n"

    # Append the entry to the text file
    with open("log.txt", "a") as file:
        file.write(entry)

# Initialize session state
if 'cookie_agreement' not in st.session_state:
    st.session_state['cookie_agreement'] = False

# Placeholder for main content
main_content = st.empty()

if st.session_state['cookie_agreement']:
    # Check if the scores file exists in session state
    if 'user_scores' not in st.session_state:
        st.session_state['user_scores'] = pd.DataFrame(columns=['Date', 'Total_Score'])

    # Display the main content of the page
    with main_content.container():
        # Update the line graph with the existing data
        scores_df = st.session_state.user_scores
        st.line_chart(scores_df.set_index('Date'))

        st.title("Welcome to Missionary Mental Health - Metamorphosis. This is the Home Page")

        # Create a form for ranking categories
        st.subheader("Over the last 2 weeks, how often have you been bothered by any of the following problems?")

        # Define categories and corresponding point values
        categories = ["Little interest or pleasure in doing things", "Feeling down, depressed or hopeless", "Trouble falling or staying asleep, or sleeping too much", "Feeling tired or having little energy", "Poor appetite or overeating", "Feeling bad about yourself - or that you are a failure or have let yourself or your family down", "Trouble concentrating on things, such as reading the newspaper or watching television", "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", "Thoughts that you would be better off dead, or of hurting yourself in some way", "Feeling nervous, anxious or on edge", "Not being able to stop or control worrying", "Worrying too much about different things", "Trouble relaxing", "Being so restless that it is hard to sit still", "Becoming easily annoyed or irritable", "Feeling afraid, as if something awful might happen"]

        point_values = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

        # Create a dictionary to store user rankings
        user_rankings = {}

        # Create a form for ranking
        for category in categories:
            user_rankings[category] = st.radio(f"{category}", options=list(point_values.keys()))

        # Submit button
        if st.button("Submit Rankings"):
            # Calculate total score
            total_score = sum(point_values[ranking] for ranking in user_rankings.values())

            text_to_append = "Home Page - Submit Rankings submit at"
            append_to_file(text_to_append)

            # Display user rankings and total score
            st.success("Rankings Submitted!")
            st.write("User Rankings:")
            for category, ranking in user_rankings.items():
                st.write(f"{category}: {ranking}")
            st.write(f"Total Score: {total_score}")

            # Update the line graph with the new data
            today_date = pd.to_datetime("today").strftime("%b %d, %Y")
            scores_df = scores_df.append({'Date': today_date, 'Total_Score': total_score}, ignore_index=True)

            # Plot the line chart
            st.line_chart(scores_df.set_index('Date'))

            # Save the scores to a file in session state
            st.session_state.user_scores = scores_df
else:
    # Overlay the cookie policy agreement
    with main_content.container():
        st.title("Cookie Policy Agreement")
        st.write("We use cookies to improve your experience on our site. Please agree to our cookie policy to continue.")
        if st.button("I agree to the cookie policy"):
            st.session_state['cookie_agreement'] = True
            st.experimental_rerun()
            text_to_append = "Cookie Policy hit at"
            append_to_file(text_to_append)

import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(
    page_title='Metamorphosis',
    layout='wide'
)

# Initialize session state
if 'cookie_agreement' not in st.session_state:
    st.session_state['cookie_agreement'] = False

# Initialize user scores in session state with hardcoded scores if empty
if 'user_scores' not in st.session_state or st.session_state.user_scores.empty:
    hardcoded_scores = [{'Date': 'Dec 1, 2023', 'Total_Score': 15},
                        {'Date': 'Dec 2, 2023', 'Total_Score': 35},
                        {'Date': 'Dec 3, 2023', 'Total_Score': 25}]
    st.session_state.user_scores = pd.DataFrame(hardcoded_scores)

# Placeholder for main content
main_content = st.empty()

# Check if the user has agreed to the cookie policy
if not st.session_state['cookie_agreement']:
    with main_content.container():
        st.title("Cookie Policy Agreement")
        st.write("We use cookies to improve your experience on our site. Please agree to our cookie policy to continue.")
        if st.button("I agree to the cookie policy"):
            st.session_state['cookie_agreement'] = True
            st.experimental_rerun()
else:
    with main_content.container():
        st.title("Welcome to Missionary Mental Health - Metamorphosis. This is the Home Page")

        # Use session state DataFrame for persistent data
        scores_df = st.session_state.user_scores

        # Display the chart
        chart = st.altair_chart(alt.Chart(scores_df).mark_line().encode(
            x=alt.X('Date:T', axis=alt.Axis(format='%b %d, %Y', labelAngle=-45)),
            y='Total_Score:Q'
        ).properties(width=800, height=400).interactive())

        st.subheader("Over the last 2 weeks, how often have you been bothered by any of the following problems?")
        categories = ["Little interest or pleasure in doing things", "Feeling down, depressed or hopeless", "Trouble falling or staying asleep, or sleeping too much", "Feeling tired or having little energy", "Poor appetite or overeating", "Feeling bad about yourself - or that you are a failure or have let yourself or your family down", "Trouble concentrating on things, such as reading the newspaper or watching television", "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", "Thoughts that you would be better off dead, or of hurting yourself in some way", "Feeling nervous, anxious or on edge", "Not being able to stop or control worrying", "Worrying too much about different things", "Trouble relaxing", "Being so restless that it is hard to sit still", "Becoming easily annoyed or irritable", "Feeling afraid, as if something awful might happen"]  # Same categories as before
        point_values = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}  # Ensure this is a dictionary

        user_rankings = {}
        for category in categories:
            # Use the category itself as a unique key for the radio buttons
            user_rankings[category] = st.radio(
                f"{category}", 
                options=list(point_values.keys()), 
                key=category  # Unique key for each category
            )

        if st.button("Submit Rankings"):
            total_score = sum(point_values[ranking] for ranking in user_rankings.values())
            today_date = pd.to_datetime("today").strftime("%b %d, %Y")
            existing_index = scores_df[scores_df['Date'] == today_date].index

            if not existing_index.empty:
                overwrite_score = st.confirm(f"You have already submitted a score for {today_date}. Do you want to overwrite it?")
                if overwrite_score:
                    scores_df.loc[existing_index, 'Total_Score'] = total_score
            else:
                new_score_entry = pd.DataFrame({'Date': [today_date], 'Total_Score': [total_score]})
                scores_df = pd.concat([scores_df, new_score_entry], ignore_index=True)

            st.session_state.user_scores = scores_df

            updated_chart = alt.Chart(scores_df).mark_line().encode(
                x=alt.X('Date:T', axis=alt.Axis(format='%b %d, %Y', labelAngle=-45)),
                y='Total_Score:Q'
            ).properties(width=800, height=400).interactive()

            chart.altair_chart(updated_chart)
            st.success("Rankings Submitted")


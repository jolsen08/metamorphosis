import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Function to save entry to CSV
def save_to_csv(title, date, text):
    # Format the date to Month-Day-Year
    formatted_date = datetime.strftime(date, '%Y-%m-%d')

    entry = pd.DataFrame([{'Title': title, 'Date': formatted_date, 'Text': text}])
    
    if os.path.exists('journal_entries.csv'):
        df = pd.read_csv('journal_entries.csv')
    else:
        df = pd.DataFrame(columns=['Title', 'Date', 'Text'])
    
    df = pd.concat([df, entry], ignore_index=True)
    df.to_csv('journal_entries.csv', index=False)

# Function to filter entries based on title and date
def filter_entries(df, title_filter, date_filter):
    filtered_df = df.copy()

    # Ensure 'Date' is in Month-Day-Year format
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%Y-%m-%d', errors='coerce')

    if title_filter:
        filtered_df = filtered_df[filtered_df['Title'].str.contains(title_filter, case=False)]
    
    if date_filter:
        # Convert the date_filter to the same format
        date_filter = datetime.strptime(date_filter, '%Y-%m-%d').date()
        filtered_df = filtered_df[filtered_df['Date'].dt.date == date_filter]
    
    return filtered_df

# Streamlit app
def main():
    st.title("Journal App")

    # Initialize session state for date filter if not present
    if 'date_filter' not in st.session_state:
        st.session_state['date_filter'] = None

    # Sidebar
    st.sidebar.header("Filters")
    title_filter = st.sidebar.text_input("Filter by Title:")

    # Date input with a key to link it to the session state
    date_filter = st.sidebar.date_input("Filter by Date:", key='date_filter')

    # Form for adding entries
    st.header("Add Entry")
    title = st.text_input("Title:")
    date = st.date_input("Date:")
    text = st.text_area("Journal Entry:", height=200)
    if st.button("Save Entry"):
        save_to_csv(title, date, text)
        st.success("Entry saved successfully!")

    # View Entries button
    if st.button("View Entries", key='view_entries'):
        st.header("Journal Entries")

        # Read CSV and filter entries
        if os.path.exists('journal_entries.csv'):
            df = pd.read_csv('journal_entries.csv', parse_dates=['Date'])
            # Use the session state variable for filtering
            filtered_df = filter_entries(df, title_filter, st.session_state['date_filter'])

            # Display filtered entries
            for index, row in filtered_df.iterrows():
                st.subheader(f"Title: {row['Title']}")
                st.write(f"Date: {row['Date'].strftime('%Y-%m-%d')}")
                st.write(row['Text'])
                st.markdown("---")
        else:
            st.info("No entries found.")

if __name__ == "__main__":
    main()
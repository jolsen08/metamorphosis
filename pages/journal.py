import streamlit as st
import pandas as pd
from datetime import datetime
import os
from home_page import append_to_file

# Function to save entry to CSV
def save_to_csv(title, date, text):
    entry = {'Title': title, 'Date': date, 'Text': text}
    
    # Check if the file exists
    if os.path.exists('journal_entries.csv'):
        df = pd.read_csv('journal_entries.csv', parse_dates=['Date'], index_col=0)
    else:
        df = pd.DataFrame(columns=['Title', 'Date', 'Text'])
    
    df = df.append(entry, ignore_index=True)
    df.to_csv('journal_entries.csv', index=False)

# Function to filter entries based on title and date
def filter_entries(df, title_filter, date_filter):
    filtered_df = df.copy()
    
    if title_filter:
        filtered_df = filtered_df[filtered_df['Title'].str.contains(title_filter, case=False)]
    
    if date_filter:
        date_filter = datetime.strptime(date_filter, '%Y-%m-%d').date()
        filtered_df = filtered_df[filtered_df['Date'].dt.date == date_filter]
    
    return filtered_df

# Streamlit app
def main():
    st.title("Journal App")

    # Sidebar
    st.sidebar.header("Filters")
    title_filter = st.sidebar.text_input("Filter by Title:")
    date_filter = st.sidebar.date_input("Filter by Date:")

    # Form for adding entries
    st.header("Add Entry")
    title = st.text_input("Title:")
    date = st.date_input("Date:")
    text = st.text_area("Journal Entry:", height=200)
    if st.button("Save Entry"):
        save_to_csv(title, date, text)
        st.success("Entry saved successfully!")
        text_to_append = "Journal - Save Entry at"
        append_to_file(text_to_append)

    # View Entries button
    if st.button("View Entries", key='view_entries'):
        st.header("Journal Entries")
        text_to_append = "Journal - View Entries at"
        append_to_file(text_to_append)

        # Read CSV and filter entries
        if os.path.exists('journal_entries.csv'):
            df = pd.read_csv('journal_entries.csv', parse_dates=['Date'])
            filtered_df = filter_entries(df, title_filter, str(date_filter))

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



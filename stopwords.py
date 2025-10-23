import streamlit as st
import pandas as pd
from io import StringIO

st.title("Stopwords Selection Tool")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Display basic info
    st.write(f"Total terms: {len(df)}")

    # Initialize session state for selections
    if 'selected_stopwords' not in st.session_state:
        st.session_state.selected_stopwords = set()

    # Search/filter functionality
    search = st.text_input("Search terms", "")

    # Filter dataframe based on search
    if search:
        filtered_df = df[df['term'].str.contains(search, case=False, na=False)]
    else:
        filtered_df = df

    st.write(f"Showing {len(filtered_df)} terms")

    # Create checkboxes for each term
    for idx, row in filtered_df.iterrows():
        term = row['term']
        freq = row['frequency']

        # Check if term is in selected stopwords
        is_checked = term in st.session_state.selected_stopwords

        # Create checkbox
        checked = st.checkbox(
            f"{term} (frequency: {freq:,})",
            value=is_checked,
            key=f"check_{idx}"
        )

        # Update selection
        if checked and term not in st.session_state.selected_stopwords:
            st.session_state.selected_stopwords.add(term)
        elif not checked and term in st.session_state.selected_stopwords:
            st.session_state.selected_stopwords.discard(term)

    # Show selected count
    st.write(f"**Selected stopwords: {len(st.session_state.selected_stopwords)}**")

    # Export functionality
    if st.session_state.selected_stopwords:
        # Create stopwords text
        stopwords_text = "\n".join(sorted(st.session_state.selected_stopwords))

        # Download button
        st.download_button(
            label="Download stopwords.txt",
            data=stopwords_text,
            file_name="stopwords.txt",
            mime="text/plain"
        )

        # Show preview
        with st.expander("Preview stopwords.txt"):
            st.text(stopwords_text)

    # Clear selection button
    if st.button("Clear all selections"):
        st.session_state.selected_stopwords = set()
        st.rerun()
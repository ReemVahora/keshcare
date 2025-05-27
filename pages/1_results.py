import streamlit as st

st.subheader("Your Results")

if st.session_state.results:
    st.write(st.session_state.results.replace("✓", ""))
else:
    st.warning("No results found. Please complete the quiz first.")
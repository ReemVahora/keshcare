import streamlit as st
import prompts

st.set_page_config(page_title="KeshCare", page_icon="🪷")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
# if results tab is visible from the start
if "results" not in st.session_state:
    st.session_state.results = prompts.testResults()

st.markdown('<h1 class="custom-title">KeshCare</h1>', unsafe_allow_html=True)
st.write(prompts.buildHomeInfo())
if st.button("What's my Dosha? 🡪"):
    st.switch_page("pages/0_quiz.py")
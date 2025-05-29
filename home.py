import streamlit as st
import openai

import prompts

st.set_page_config(page_title="KeshCare", page_icon="🪷")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("KeshCare")
#🪷

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

st.write(prompts.buildHomeInfo())

if st.button("What's my Dosha? 🡪"):
    st.session_state.quiz_started = True
    st.switch_page("pages/0_quiz.py")

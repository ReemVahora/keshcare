import streamlit as st
import prompts
import os

st.set_page_config(page_title="KeshCare", page_icon="🪷")

css_path = "D:\Projects\keshcare\src\styles.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "results" not in st.session_state:
    st.session_state.results = []
if "results_index" not in st.session_state:
    st.session_state.results_index = 0
if "results_list" not in st.session_state:
    st.session_state.results_list = False


st.markdown('<h1 class="custom-title">KeshCare</h1>', unsafe_allow_html=True)
st.write(prompts.buildHomeInfo())
if st.button("What's my Dosha? 🡪"):
    st.switch_page("pages/0_quiz.py")
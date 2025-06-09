import streamlit as st
import prompts

from pages.utils.session import initSessionState

initSessionState()

st.set_page_config(page_title="KeshCare", page_icon="🪷", layout="centered")

with open("src/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Info & Policies")
st.markdown(prompts.buildInfo())
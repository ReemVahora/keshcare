import streamlit as st
import prompts

from pages.utils.session import initSessionState

st.set_page_config(page_title="KeshCare", page_icon="🪷", layout="centered")

initSessionState()

with open("src/styles.css") as base, open("src/styles-title.css") as title_page:
    st.markdown(
        f"<style>{base.read()}\n{title_page.read()}</style>", 
                unsafe_allow_html=True)

st.markdown('<h1 class="custom-title">KeshCare</h1>', unsafe_allow_html=True)
st.write(prompts.buildHomeInfo())
if st.button("What's my Dosha?"):
    st.switch_page("pages/0_Quiz.py")

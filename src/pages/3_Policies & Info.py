import streamlit as st
import prompts

st.set_page_config(page_title="KeshCare", page_icon="🪷")

with open("src/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Info & Policies")
st.markdown(prompts.buildInfo())
import streamlit as st
import prompts
import os

st.set_page_config(page_title="KeshCare", page_icon="🪷")

css_path = "D:\Projects\keshcare\src\styles.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Info & Policies")
st.markdown(prompts.buildInfo())
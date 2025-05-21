import streamlit as st
import openai
import prompts

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="KeshCare", page_icon="🪷")
st.title("KeshCare🍃")
st.write("[INSERT INTRO HERE]")
st.button("Start Quiz 🡪")

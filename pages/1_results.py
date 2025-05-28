import streamlit as st
import pandas as pd
import plotly.express as px
import re
import json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

st.title("Your Results")

if st.session_state.results:
    results = st.session_state.results

    # extract and clean
    data_list = re.findall(r"\{.*?\}", results)
    data_extract = data_list[0]
    results = results.replace("✓", "").replace(data_extract, "")
    
    # load pie chart
    pie_data = json.loads(data_extract)

    df = pd.DataFrame({
        'Dosha': list(pie_data.keys()),
        'Percentage': list(pie_data.values())
    })

    fig = px.pie(df, names='Dosha', values='Percentage', color_discrete_sequence=['#A67B5B', '#C2B280', '#8B6E4A'], title="Your Dosha Composition")
    st.plotly_chart(fig, use_container_width=True)

    st.write(results)

else:
    st.warning("No results found. Please complete the quiz first.")

if st.button("Back to Chat", key="back_to_chat_button"):
    st.switch_page("app.py")
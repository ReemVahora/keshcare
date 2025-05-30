import streamlit as st
import pandas as pd
import plotly.express as px
import re
import json

st.set_page_config(page_title="KeshCare", page_icon="🪷")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Your Results")

if st.session_state.results:
    results = st.session_state.results

    # extract and clean
    data_list = re.findall(r"\{.*?\}", results)
    init_string = data_list[0].replace("{", "").replace("}", "")
    data_extract = data_list[1]
    results = results.replace("✓", "").replace(data_extract, "").replace(init_string, "").replace("{", "").replace("}", "")
    
    # init string
    st.write(init_string)

    # load pie chart
    pie_data = json.loads(data_extract)

    df = pd.DataFrame({
        'Dosha': list(pie_data.keys()),
        'Percentage': list(pie_data.values())
    })
    dosha_colors = {
    "Vata": "#A8B0A2",
    "Pitta": "#A7A985",
    "Kapha": "#8C5C4E"
    }

    fig = px.pie(df,
                 names='Dosha',
                 values='Percentage',
                 color="Dosha",
                 color_discrete_map=dosha_colors,
                 title="Your Dosha Composition"
                 )
    st.plotly_chart(fig, use_container_width=True)

    # rest of results
    st.write(results)

else:
    st.warning("No results found. Please complete the quiz first.")

if st.button("Back", key="back_button"):
    st.switch_page("pages/0_quiz.py")
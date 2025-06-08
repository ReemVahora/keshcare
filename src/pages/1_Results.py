import streamlit as st
import pandas as pd
import plotly.express as px
import re
import json

st.set_page_config(page_title="KeshCare", page_icon="🪷")

with open("src/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#####################################################################################
#Abstracted methods

def printPieChart(data_extract):
    # load pie data
    pie_data = json.loads(data_extract)

    df = pd.DataFrame({
        'Dosha': list(pie_data.keys()),
        'Percentage': list(pie_data.values())
    })

    # Pie chart attributes
    dosha_colors = {
    "Vata": "#A1BFBC",
    "Pitta": "#E7906B",
    "Kapha": "#BAC568"
    }
    fig = px.pie(df,
                    names='Dosha',
                    values='Percentage',
                    color="Dosha",
                    color_discrete_map=dosha_colors,
                    title="Your Dosha Composition"
                    )
    fig.update_traces(
        textposition='inside',
        textinfo='label+percent',
        insidetextfont=dict(size=15, family='Georgia')
    )
    fig.update_traces(marker=dict(line=dict(color='#F5ECE0', width=2.5)))
    fig.update_layout(
        title={
        'font': {'size': 28},
        'x': 0.5,
        'xanchor': 'center'
        },
        paper_bgcolor='rgba(0,0,0,0)',
        height=500,
        width=500,
        showlegend=False,
    )

    st.plotly_chart(fig, use_container_width=True)


def printResults(index):
    results = st.session_state.results[index]

    # extract and clean
    data_list = re.findall(r"\{.*?\}", results) 
    init_string = data_list[0].replace("{", "").replace("}", "")
    data_extract = data_list[1]
    results = results.replace("✓", "").replace(data_extract, "").replace(init_string, "").replace("{", "").replace("}", "")
    
    st.write(init_string) # initial para
    printPieChart(data_extract)
    
    st.write(results) # rest of results

    # button to display results list
    if len(st.session_state.results) > 1:
        if st.button("All results", key="results_list_button"):
            st.session_state.results_list = True
            st.rerun()



def displayResultsList():
    if len(st.session_state.results) == 1:
        printResults(0)
    for i in reversed(range(0, len(st.session_state.results))):
        with col2:
            if st.button("Your Results - #" + str(i+1)):
                st.session_state.results_list = False
                st.session_state.results_index = i
                st.rerun()
    if st.button("Quiz", key="quiz_button"):
        st.switch_page("pages/0_Quiz.py")


########################################################################################


st.title("Your Results")
col1, col2, col3 = st.columns([3, 2, 3])

if len(st.session_state.results) == 0:
    st.warning("No results found. Please complete the quiz first.")
elif st.session_state.results_list:
    displayResultsList()
else: 
    printResults(st.session_state.results_index-1)

if st.button("Quiz", key="quiz_button"):
    st.switch_page("pages/0_Quiz.py")
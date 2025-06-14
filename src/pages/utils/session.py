import streamlit as st
import prompts

def initSessionState():
    defaults = {
        "quiz_started" : False,
        "awaiting_response" : True,
        "chat_history" : [
        {"role": "system", "content": prompts.buildSystemPrompt()},
        {"role": "system", "content": f"Here is a list of ayurvedic ingredients and practises you might find handy: {prompts.getGlossary()}"},
        {"role": "user", "content": "Hi, I'm ready for the introduction."},
        {"role": "assistant", "content": prompts.buildIntro()}
        ],
        "results" : [],
        "results_index" : -1,
        "results_list" : False
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
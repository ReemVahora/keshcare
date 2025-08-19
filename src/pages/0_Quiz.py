import streamlit as st
import openai
import streamlit.components.v1 as components

from pages.utils.session import initSessionState 
from pages.utils.helpers import copy_button

initSessionState()

st.set_page_config(page_title="KeshCare", page_icon="🪷", layout="centered")

with open("src/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.session_state.quiz_started = True

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#############################################################################################################

# Abstracted methods

def scroll_down():
    components.html(
    """
    <div id="autoscroll-anchor">
    <script>
        document.getElementById("autoscroll-anchor").scrollIntoView({behavior: "smooth"});
    </script>
    </div>
    """,
    height=300,
)

def display_chat_history():
    for i, msg in enumerate(st.session_state.chat_history[3:]):
        if "✓" in msg["content"]:
            st.chat_message(msg["role"]).write("Your results are ready below! Any questions or concerns?")
            if st.button("View Results", key=f"view_results_btn_{i}"):
                st.switch_page("pages/1_Results.py")
        else:
            st.chat_message(msg["role"]).write(msg["content"])
            copy_button(msg["content"])


def user_input_logic(user_input):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.awaiting_response = False  #turn off while bot responds
        scroll_down()
        st.rerun()


def bot_response_logic(user_input):
    with st.spinner("Thinking..."):                                                                                                                                                                                                                                     
        #Calling OpenAI API here using chat_history
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages = st.session_state.chat_history,
            temperature=0.7,
            max_tokens=750
        )
        bot_reply = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        scroll_down()
    
    if "✓" in bot_reply:
        st.session_state.results.append(bot_reply)
        st.session_state.results_index += 1
    
    st.session_state.awaiting_response = True
    st.rerun()
        
    
#############################################################################################################

# Will come back here every rerun

if st.session_state.quiz_started:
    display_chat_history()

    user_input = st.chat_input("Your response")
    
    if st.session_state.awaiting_response: user_input_logic(user_input)
    else: bot_response_logic(user_input)

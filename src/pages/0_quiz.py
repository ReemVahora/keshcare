import streamlit as st
import openai
import uuid

import prompts

st.session_state.quiz_started = True

st.set_page_config(page_title="KeshCare", page_icon="🪷")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": prompts.buildSystemPrompt()},
        {"role": "system", "content": f"Here is a list of ayurvedic ingredients and practises you might find handy: {prompts.getGlossary()}"},
        {"role": "user", "content": "Hi, I'm ready for the introduction."},
        {"role": "assistant", "content": prompts.buildIntro()}
    ]
if "awaiting_response" not in st.session_state:
    st.session_state.awaiting_response = True


#############################################################################################################

# Abstracted methods




def copy_button(text: str):
    # Unique ID for each button to avoid conflicts
    button_id = str(uuid.uuid4()).replace("-", "")
    html_code = f"""
    <button id="{button_id}" style="
        background-color:#eee;
        float: right;
        border:none;
        padding:5px 5px;
        margin-top: -12px;
        cursor:pointer;j
        font-size:16px;
        border-radius:2px;
    ">📋</button>
    <script>
    const btn = document.getElementById("{button_id}");
    btn.onclick = () => {{
        navigator.clipboard.writeText({text!r}).then(() => {{
            btn.textContent = '✔️';
            setTimeout(() => btn.textContent = '📋', 1500);
        }});
    }};
    </script>
    """
    st.components.v1.html(html_code, height=30)

# # Example usage:
# with st.chat_message("assistant"):
#     message = "Here is some helpful message text you want to copy."
#     st.markdown(message)
#     copy_button(message)



def display_chat_history():
    for i, msg in enumerate(st.session_state.chat_history[3:]):
        if "✓" in msg["content"]:
            st.chat_message(msg["role"]).write("Your results are ready below! Any questions or concerns?")
            if st.button("View Results", key=f"view_results_btn_{i}"):
                st.switch_page("pages/1_results.py")
        else:
            st.chat_message(msg["role"]).write(msg["content"])
            copy_button(msg["content"])

def user_input_logic(user_input):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.awaiting_response = False  #turn off while bot responds
        st.rerun()

def bot_response_logic(user_input):
    with st.spinner("Thinking..."):
        #Calling OpenAI API here using chat_history
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages = st.session_state.chat_history,
            temperature=0.7,
            max_tokens=500
        )
        bot_reply = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
    
    if "✓" in bot_reply:
        st.session_state.results = bot_reply
    
    st.session_state.awaiting_response = True
    st.rerun()
        
    
#############################################################################################################

# Will come back here every rerun

if st.session_state.quiz_started:
    display_chat_history()

if st.session_state.quiz_started:
    # user input only here once, so problem fixed. 
    user_input = st.chat_input("Your response")
    
    if st.session_state.awaiting_response: user_input_logic(user_input)
    else: bot_response_logic(user_input)

# YALL IT WORKSSSSS
import streamlit as st
import openai
import prompts

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="KeshCare", page_icon="🪷")
st.title("KeshCare🍃")
results = ""


#Initializing session states
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": prompts.buildSystemPrompt()},
        {"role": "user", "content": "Hi, I'm ready to begin the hair quiz."}
    ]
if "awaiting_response" not in st.session_state:
    st.session_state.awaiting_response = False


if not st.session_state.quiz_started:
    st.write("[INSERT INTRO HERE]")
    if st.button("Start Quiz 🡪"):
        st.session_state.quiz_started = True
        st.rerun()

for msg in st.session_state.chat_history[2:]:
    st.chat_message(msg["role"]).write(msg["content"])


#############################################################################################################
#Abstracted methods so that they can jump back and forth

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
        st.write(f"AI: {bot_reply}")

    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})    
    
    st.session_state.awaiting_response = True
    user_input_logic(user_input)
        
    if "✓" in bot_reply:
        results = bot_reply

    #     st.session_state.awaiting_response = True
    #     user_input_logic(user_input)
    
#############################################################################################################
#Will come back here every rerun

if st.session_state.quiz_started:
    #user input only here once, so problem fixed. 
    user_input = st.chat_input("Your response")
    
    if st.session_state.awaiting_response: user_input_logic(user_input)
    else: bot_response_logic(user_input)

import streamlit as st
import openai
import prompts

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="KeshCare", page_icon="🪷")
st.title("KeshCare🍃")
st.write("[INSERT INTRO HERE]")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": prompts.buildSystemPrompt()},
        {"role": "user", "content": "Hi, I'm ready to begin the hair quiz."}
    ]

#while True loop is becoming an issue lol
if st.button("Start Quiz 🡪"):
    while True:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=st.session_state.chat_history,
            temperature=0.7,
            max_tokens=500
        )
        bot_reponse = response.choices[0].message.content
        st.write(f"AI: {bot_reponse}")

        if "✓" in bot_reponse:
            st.write("Loop endedddddd")
            break

        st.session_state.chat_history.append({"role": "assistant", "content": bot_reponse})
        user_input = st.text_input("Your response: ")
        if user_input:
            st.write("booooooyaaah")
            st.session_state.chat_history.append({"role": "user", "content": user_input})


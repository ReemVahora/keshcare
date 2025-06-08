import streamlit as st
import prompts

st.set_page_config(page_title="KeshCare", page_icon="🪷")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Info & Policies")
st.markdown(prompts.buildInfo())

# st.write("This app is created as a passion project to guide self-awareness through personalized Ayurvedic insights. It offers a gentle, educational approach rooted in traditional wisdom, helping you explore your dosha constitution with respect and care.")
# st.subheader("Privacy & Data Use")
# st.write("Your privacy is our priority. We **do not collect, store, or share any personal information**, including names or emails. All quiz responses remain local on your device and are used solely to provide your personalized results during your session.")
# st.subheader("Terms of Use")
# st.write("This app is designed for **educational and informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Please consult a qualified healthcare provider for personalized medical guidance.")
# st.subheader("Contact")
# st.write("""Questions or feedback?\n\n Feel free to reach out via email:
# **\[[vahora.reem@gmail.com](mailto:vahora.reem@gmail.com)]**""")
# st.subheader("Accessibility Commitment")
# st.write("We strive to make this app welcoming and accessible to everyone. If you experience any difficulties or have suggestions to improve accessibility, please contact us.")
# st.write("Thank you for trusting this space to explore your wellness. May your journey be insightful and balanced.")

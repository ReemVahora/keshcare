import streamlit as st

st.title("🌿 Ayurvedic Ingredient Glossary")

glossary = {
    "Amla": "Rich in Vitamin C, promotes hair growth and strengthens follicles.",
    "Bhringraj": "Known as the 'king of herbs' for hair, it prevents hair loss and promotes regrowth.",
    "Neem": "Antibacterial and antifungal, helps with dandruff and scalp health.",
    "Brahmi": "Improves circulation to the scalp and strengthens hair roots.",
    "Shikakai": "A natural cleanser that maintains scalp moisture and reduces itchiness.",
    "Ashwagandha": "Helps reduce stress-related hair fall.",
}

for herb, definition in glossary.items():
    st.subheader(herb)
    st.write(definition)

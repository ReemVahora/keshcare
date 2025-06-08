import streamlit as st
import re
import prompts
import os

st.set_page_config(page_title="KeshCare", page_icon="🪷")

css_path = "D:\Projects\keshcare\src\styles.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Glossary")
glossary = prompts.getGlossary()
glossary = dict(sorted(glossary.items()))

# Category mapping
categories = {
    "Herbs & Botanicals": [
        "Amla", "Bhringraj", "Brahmi", "Neem", "Hibiscus", "Fenugreek", "Shikakai",
        "Reetha", "Aloe Vera", "Ashwagandha", "Licorice Root (Yashtimadhu)", "Curry Leaves",
        "Tulsi (Holy Basil)", "Vetiver", "Nagarmotha (Cyperus Rotundus)", "Maka (Eclipta Alba)", "Kapur Kachri",
        "Henna", "Indigo", "Manjistha", "Guduchi (Giloy)", "Kalmegh", "Triphala", "Chyawanprash"
    ],
    "Oils & Carriers": [
        "Sesame Oil", "Coconut Oil", "Castor Oil", "Mustard Oil", "Almond Oil", "Tea Tree Oil",
        "Rosemary Oil", "Lavender Oil", "Peppermint Oil", "Lemongrass Oil", "Cedarwood Oil",
        "Brahmi Ghee", "Rosewater"
    ],
    "Ayurvedic Therapies & Routines": [
        "Shiroabhyanga", "Abhyanga", "Nasya", "Shirodhara", "Takradhara", "Panchakarma", "Basti",
        "Dinacharya", "Ritucharya"
    ],
    "Doshas & Diagnostic Concepts": [
        "Vata", "Pitta", "Kapha", "Tridoshic", "Prakriti", "Vikriti", "Ojas", "Tejas", "Agni",
        "Ama", "Rasa Dhatu", "Srotas", "Vaidya"
    ],
    "Supplements & Internal Use": [
        "Ashwagandha Capsules", "Brahmi Ghee", "Triphala", "Chyawanprash", "Rosewater"
    ]
}

categories = dict(sorted(categories.items()))

# selector
selected_categories = st.multiselect(
    "",
    options=list(categories.keys()),
    placeholder="Filter by Category",
    default=[]
)

# filtered list
if selected_categories:
    filtered_keys = set()
    for cat in selected_categories:
        filtered_keys.update(categories[cat])
else:
    filtered_keys = set(glossary.keys())  # show all if no filter

###################################################################################################
# abstracted functions

def highlight_text(text, keyword):
    if keyword.strip() == "":
        return text
    keyword_lower = keyword.lower()
    return text.replace(
        keyword,
        f"<mark>{keyword}</mark>"
    ).replace(
        keyword.capitalize(),
        f"<mark>{keyword.capitalize()}</mark>"
    ).replace(
        keyword_lower,
        f"<mark>{keyword_lower}</mark>"
    )

# search priority sorter
def score_result(key, value, query):
    pattern = r'\b{}\b'.format(re.escape(query.lower()))  # whole word pattern
    title = key.lower()
    desc = value.lower()

    if re.search(pattern, title):
        return 4  # highest priority: exact whole word in title
    elif re.search(pattern, desc):
        return 3  # whole word in definition
    elif query.lower() in title:
        return 2  # partial in title
    elif query.lower() in desc:
        return 1  # partial in definition
    else:
        return 0  # no match

###################################################################################################

# Search bar
query = st.text_input("", placeholder="Search ingredients, concerns, buzzwords...")

# filter
if query:
    results = {
        k: glossary[k]
        for k in filtered_keys
        if query.lower() in k.lower() or query.lower() in glossary[k].lower()}
    # priority (4 to 0), and alphabetical order within each
    results = dict(
    sorted(sorted(results.items()), key=lambda item: score_result(item[0], item[1], query), reverse=True))
    if results:
        for ingredient, definition in results.items():
            highlighted_term = highlight_text(ingredient, query)
            highlighted_definition = highlight_text(definition, query)

            st.markdown(f"### {highlighted_term}", unsafe_allow_html=True)
            st.markdown(f"<p>{highlighted_definition}</p>", unsafe_allow_html=True)
    else:
        st.info("No matching terms found.")
else:
    for key in sorted(filtered_keys):
        st.subheader(f"**{key}**")
        st.write(glossary[key])

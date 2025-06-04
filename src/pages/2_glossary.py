import streamlit as st
import re

st.set_page_config(page_title="KeshCare", page_icon="🪷")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Glossary")

glossary = {
    "Amla": "Indian gooseberry rich in Vitamin C; strengthens roots, promotes hair growth, and prevents premature greying.",
    "Bhringraj": "Known as 'King of Herbs' for hair; revitalizes hair follicles, reduces hair fall, and promotes thicker growth.",
    "Brahmi": "Cooling herb that strengthens hair, prevents split ends, and calms the scalp to reduce dandruff and stress-related hair fall.",
    "Neem": "Antibacterial and antifungal; treats dandruff, scalp infections, and balances oil production.",
    "Hibiscus": "Rich in amino acids; promotes hair growth, conditions hair, and prevents premature greying and split ends.",
    "Fenugreek": "Protein and nicotinic acid-rich seeds; reduce hair fall, fight dandruff, and add shine and softness.",
    "Shikakai": "Natural cleanser; gently cleanses scalp without stripping oils, promotes growth, and detangles hair.",
    "Reetha": "Soapnut with natural saponins; cleanses scalp, adds volume, and maintains scalp pH balance.",
    "Aloe Vera": "Soothes itchy scalp, reduces dandruff, deeply hydrates hair, and strengthens strands.",
    "Ashwagandha": "Adaptogenic herb; reduces cortisol-related hair loss and supports melanin production to delay greying.",
    "Licorice Root (Yashtimadhu)": "Soothes scalp irritation, reduces dandruff, and promotes healthy follicle function.",
    "Curry Leaves": "Rich in antioxidants and beta-carotene; strengthens hair and slows greying.",
    "Tulsi (Holy Basil)": "Antibacterial and antifungal; improves circulation and keeps scalp healthy.",
    "Vetiver": "Cooling and grounding; promotes thick hair growth and balances excess pitta on the scalp.",
    "Nagarmotha (Cyperus Rotundus)": "Balances sebum production; helps with oily scalp and hair thinning.",
    "Maka (Eclipta Alba)": "Often used interchangeably with Bhringraj; nourishes roots and supports regrowth.",
    "Kapur Kachri": "Aromatic root used to boost hair shine, improve texture, and fight scalp infections.",
    "Aritha (Soapnut)": "Similar to Reetha; cleanses without chemicals, suitable for sensitive scalps.",
    "Sesame Oil": "Warming and nourishing oil; deeply penetrates the scalp to strengthen hair and promote growth.",
    "Coconut Oil": "Cooling and antimicrobial; deeply moisturizes, prevents protein loss, and promotes strong hair.",
    "Castor Oil": "Thick and deeply nourishing; stimulates hair growth and thickens thinning areas.",
    "Mustard Oil": "Stimulates blood flow to the scalp, warms follicles, and supports growth.",
    "Almond Oil": "Rich in Vitamin E and magnesium; strengthens strands and improves shine.",
    "Jatamansi": "Calms the nervous system; reduces stress-related hair fall and supports hair darkening.",
    "Manjistha": "Blood purifier; supports scalp detoxification and reduces inflammation.",
    "Henna": "Natural dye and conditioner; strengthens hair, improves texture, and covers greys with a reddish tint.",
    "Indigo": "Herb that provides deep blue-black tint; often used with henna to naturally darken hair.",
    "Guduchi (Giloy)": "Adaptogen and detoxifier; improves scalp immunity and supports overall follicle health.",
    "Kalmegh": "Bitter detoxifying herb; purifies blood, supports scalp health, and may help with inflammation and hair loss linked to toxins.",
    "Tea Tree Oil": "Essential oil with powerful antifungal and antibacterial properties; treats dandruff and itchy scalp. Must be diluted before topical use.",
    "Rosemary Oil": "Stimulates blood circulation to the scalp; encourages hair growth and thickness. Must be diluted before topical use.",
    "Lavender Oil": "Soothes scalp inflammation and promotes hair regrowth; also helps reduce stress. Must be diluted before topical use.",
    "Peppermint Oil": "Cooling essential oil that improves scalp circulation and may promote faster hair growth. Must be diluted before topical use.",
    "Lemongrass Oil": "Antimicrobial and astringent; helps with dandruff and keeps scalp clean. Must be diluted before topical use.",
    "Cedarwood Oil": "Balances oil production on the scalp and supports hair follicle strength. Must be diluted before topical use.",
    "Triphala": "A blend of Amla, Haritaki, and Bibhitaki; detoxifies the system, improves digestion and nutrient absorption, which supports hair health from within.",
    "Chyawanprash": "A herbal jam rich in Amla and other rejuvenating herbs; boosts immunity, slows ageing, and nourishes hair from the inside out.",
    "Ashwagandha Capsules": "Convenient adaptogenic supplement; helps manage stress-related hair loss and balances hormones that affect hair growth.",
    "Brahmi Ghee": "Medicated clarified butter infused with Brahmi; nourishes the brain and nervous system, reduces stress, and indirectly supports hair health when taken internally or used topically on the scalp.",
    "Rosewater": "Hydrosol made from rose petals; soothes the scalp, balances pH, reduces inflammation, and can be used as a gentle hair mist or rinse.",
    "Vata": "One of the three doshas; governs movement, dryness, and cold. Imbalanced Vata can lead to dry scalp, frizz, and brittleness.",
    "Pitta": "One of the three doshas; governs heat, metabolism, and transformation. Pitta imbalance often causes hair thinning, greying, or scalp inflammation.",
    "Kapha": "One of the three doshas; governs structure, lubrication, and growth. Excess Kapha can lead to oily scalp, buildup, and slow hair growth.",
    "Tridoshic": "A balanced state of all three doshas; products or practices labeled 'tridoshic' are generally safe and balancing for all types.",
    "Prakriti": "Your inherent dosha constitution, fixed at birth; helps determine your ideal hair care and lifestyle routine.",
    "Vikriti": "Your current doshic imbalance; guides which treatments or herbs are most appropriate at the moment.",
    "Dinacharya": "Daily Ayurvedic self-care routine; may include oil pulling, scalp massage, and mindful hair practices.",
    "Ritucharya": "Seasonal regimen; adjusting hair care according to seasonal dosha influences (e.g., hydrating more in summer to balance Pitta).",
    "Shiroabhyanga": "Ayurvedic head massage using warm herbal oils; improves blood flow, strengthens roots, and calms the mind.",
    "Nasya": "Nasal administration of herbal oils; supports brain and scalp nourishment and is sometimes used for chronic hair loss.",
    "Takradhara": "A soothing therapy where medicated buttermilk is poured over the forehead; balances Pitta and stress-related hair issues.",
    "Shirodhara": "A continuous stream of warm oil poured on the forehead; deeply calming, reduces stress-related hair loss.",
    "Panchakarma": "A five-part Ayurvedic detoxification and rejuvenation program; includes therapies like oil massage, herbal enemas, and cleansing to restore doshic balance and boost hair health.",
    "Abhyanga": "Full-body warm oil massage that improves circulation, nourishes tissues, and supports hormonal balance — all of which affect hair.",
    "Basti": "Medicated enema used during Panchakarma to cleanse the colon and support systemic detox, often improving skin and hair from within.",
    "Ojas": "Vital life essence; its preservation is crucial for lustrous, strong hair and overall vitality.",
    "Tejas": "Subtle form of Pitta; governs transformation and metabolism. Balanced Tejas supports healthy digestion and hair pigmentation.",
    "Agni": "Digestive/metabolic fire; strong agni ensures nutrient absorption and tissue nourishment, including hair.",
    "Ama": "Toxic residue from undigested food; contributes to dull, thinning hair and scalp congestion.",
    "Rasa Dhatu": "The first and most fundamental bodily tissue; nourishes all other tissues including the scalp and hair.",
    "Srotas": "Body channels; blockages here (especially in rasavaha and raktavaha srotas) can impair hair nourishment.",
    "Vaidya": "A trained Ayurvedic practitioner who diagnoses dosha imbalances and prescribes personalized treatments."    
}


def highlight_text(text, keyword):
    # Only highlight if keyword exists
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

sorted_glossary = dict(sorted(glossary.items()))

# Search bar
query = st.text_input("", placeholder="Search ingredients, concerns, buzzwords...")

# Filter and display results
if query:
    results = {k: v for k, v in glossary.items() if query.lower() in k.lower() or query.lower() in v.lower()}
    if results:
        for ingredient, definition in results.items():
            highlighted_term = highlight_text(ingredient, query)
            highlighted_definition = highlight_text(definition, query)

            st.markdown(f"### {highlighted_term}", unsafe_allow_html=True)
            st.markdown(f"<p>{highlighted_definition}</p>", unsafe_allow_html=True)

            #st.subheader(ingredient)
            #st.write(definition)
    else:
        st.info("No matching terms found.")
else:
    for ingredient, definition in sorted_glossary.items():
        st.subheader(ingredient)
        st.write(definition)

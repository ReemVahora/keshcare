# For prompts and other lengthy strings

def buildSystemPrompt():
    return """
You are Neema, an Ayurvedic haircare expert (you can refer to yourself as a 'Vaidya') trained to determine a user's hair dosha and recommend personalized treatments. 

You will ask thoughtful, respectful questions to learn about the user’s current hair condition, history, scalp health, and lifestyle.
Here are a list of questions/topics a human ayurvedic-expert would cover. DO NOT copy questions verbatim! Questions below are simply a guide. As more questions if necessary! 
Ask questions in a reasonable sensible order (not necessarily the one specified below). 
Provide warm, careful, accurate support. Keep track of user inputs internally and maintain a helpful, clear, zen and human-like tone throughout.

Topics you can explore (reword and re-order naturally):

* Hair texture (straight, wavy, curly, or coily?)
* Hair density  (sparse, medium or thick?)
* Scalp condition (dry to oily range)  
* Hair growth speed (slow to fast)  
* Hair fall frequency  
* Premature graying?  
* Natural hair color  
* Natural shine (dull, moderate, shiny)  
* Manageability  
* Reactions to weather  
* Questions regarding their hair routine and products use (if relevant)
* Hair porosity (if relevant)  
* Lifestyle/stress  (if relevant)
* Any concerns the user wants to address (MUST! offer helpful examples)

If you're unsure, continue asking targeted questions! Always verify your understanding step-by-step.
Only proceed to diagnosis when you have enough information to make a confident and accurate dosha determination (Vata, Pitta, Kapha, or a combination).

Avoid pop culture or speculative wellness trends. All advice must align with traditional Ayurvedic principles. Once the dosha is identified, give clear, practical guidance:
- Recommended oils, herbs, and ingredients
- What to avoid (e.g., harsh shampoos, wrong oils)
- Tips for routine and seasonal care

If the user's hair is only temporarily changed due to stress, weather, or illness, acknowledge that and adjust recommendations accordingly.

YOU DO NOT KNOW ANY BRANDS! NONE!

Always speak kindly, clearly, and helpfully — like a trusted wellness guide.

Start by asking one question at a time. Say 'Let’s get started!'. 
Remember to keep track of their answers before making any diagnosis.

Now for generating results, follow these following steps IN ORDER:

STEP 1 - FORMAT RESULTS INTRO (the first 1-2 sentences)

The first 1-2 sentences of the RESULTS generated will be conversationally following the user's last reponse.
Wrap up this part with curly braces, and begin with "✓".
FOR EXAMPLE;
✓{Thank you for sharing your goal of adding volume to your hair. Based on your responses about your curly, medium-density hair with a balanced scalp, and your interest in natural, organic care, let's determine the best Ayurvedic approach for you.}
See? Any conversational-continuing statements must be wrapped in curly brackets.

STEP 2 - GENERATE DOSHA PERCENTAGES

Whenever you are generating results;
You must determine percentage values of each dosha that accurately represents the user's hair dosha composition. 
Print it like this, even if any of the X, Y or Z values are 0. Don't forget the curly brackets like below:  
{"Vata": X,"Pitta": Y,"Kapha": Z}


STEP 3 - FORMAT THE REST OF THE RESULTS

For results, heed the following and use large subheadings;
Recommend oils, herbs, and natural treatments ideal for the user based on Ayurvedic principles.
List out the oils and ingredients and elaborate on how they are relevant to the user's neeeds and inner balance. 
Include a hair massaging method describing exactly what to do and how often to do it. 
Feel free to briefly elaborate and educate the user on the ingredients and ayurvedic principles and practises that could be relevant to them. 
Provide lifestyle or seasonal care tips if needed, including what to avoid.
Avoid pop culture trends. All advice must align with traditional Ayurvedic principles.
In the end provide a little feedback on their current routine and whether to keep it up, tone it down, increase frequency etc.

REGARDING RE-GENERATION OF RESULTS:
- ALWAYS ASK BEFORE DOING SO
- DO NOT REGENERATE RESULTS WITHOUT APPROVAL FROM THE USER!!!
- YOU must ask "Would you like to regenerate results?".
- YOU must also reassure the user that they will be able to access their previosu results via "All Results" button at the bottom of the results page. 
- If they say no, then do NOT REGENERATE! Answer their questions exactly in the chat without the results formatting.
- The user may provide new information that updates/changes their results, may also contradict initial answers which may prompt you to ask for a regeneration of results. 
- If you can, ask at least one more question so you have a clearer idea of their dosha composition, before asking to regenerate user's results.
- YOU MUST repeat STEP 1-3 IN ORDER, for the new results!
"""

def buildHomeInfo():
    return """
**Curious about the secrets behind traditional Indian haircare?**

Rooted in ancient wisdom and natural rhythms, Ayurveda offers a gentle yet powerful path to understanding and nurturing your hair, from the inside out. 

Ayurveda, translated from Sanskrit as “the science of life,” is a holistic system of wellness that originated in India over 5,000 years ago. Rooted in nature and balance, Ayurveda teaches that health is achieved when the body, mind, and spirit exist in harmony with the environment. At its core, it views each individual as a unique combination of the five elements- earth, water, fire, air, and ether- which form the foundation of three biological energies, or **doshas**: 

**Vata**, **Pitta**, and **Kapha**.

Each person is born with a natural constitution known as **Prakriti**, a unique balance of the doshas that shapes everything from physical characteristics to emotional tendencies and health patterns. When our doshas fall out of balance- due to lifestyle, diet, stress, or seasonal changes- we may experience unease in subtle or more apparent ways. Ayurveda helps us recognize these imbalances and gently restore alignment through mindful living and natural care.

Hair, too, is deeply influenced by the doshas. For example, a Vata imbalance may lead to dryness or frizz, Pitta to thinning or premature greying, and Kapha to heaviness or oiliness. With emphasis on oiling and massaging techniques, Ayurvedic haircare looks beyond surface-level symptoms, considering the scalp, lifestyle, digestion, and emotions as part of the hair’s health story. By understanding your **hair Prakriti**, you can nourish your hair in a way that is intentional, deeply restoring and personalized to you. 
"""

def buildIntro():
    return """
Hi, I’m Neema, your personal Ayurvedic haircare guide.🌿

This quiz is designed to help determine your unique hair dosha composition— Vata, Pitta, Kapha, or a combination— based on Ayurvedic principles. With your responses, I’ll offer personalized guidance on ingredients, oils, and holistic practices best suited for your hair type.

Feel free to share as much detail as you’d like. The more I understand, the more accurate your results will be. If at any point you’d like to revise an answer or add something new, just let me know— we can always revisit and refine your results together.🌸

Are you ready?
"""

def getGlossary():
    return {
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
        "Abhyanga": "Full-body warm oil massage that improves circulation, nourishes tissues, and supports hormonal balance, all of which affect hair.",
        "Basti": "Medicated enema used during Panchakarma to cleanse the colon and support systemic detox, often improving skin and hair from within.",
        "Ojas": "Vital life essence; its preservation is crucial for lustrous, strong hair and overall vitality.",
        "Tejas": "Subtle form of Pitta; governs transformation and metabolism. Balanced Tejas supports healthy digestion and hair pigmentation.",
        "Agni": "Digestive/metabolic fire; strong agni ensures nutrient absorption and tissue nourishment, including hair.",
        "Ama": "Toxic residue from undigested food; contributes to dull, thinning hair and scalp congestion.",
        "Rasa Dhatu": "The first and most fundamental bodily tissue; nourishes all other tissues including the scalp and hair.",
        "Srotas": "Body channels; blockages here (especially in rasavaha and raktavaha srotas) can impair hair nourishment.",
        "Vaidya": "A trained Ayurvedic practitioner who diagnoses dosha imbalances and prescribes personalized treatments."
    }


def testResults():
    return """
{Thank you for sharing your goal of adding volume to your hair. Based on your responses about your curly, medium-density hair with a balanced scalp, and your interest in natural, organic care, let's determine the best Ayurvedic approach for you.}

✓{"Vata": 30,"Pitta": 30,"Kapha": 40}
"""
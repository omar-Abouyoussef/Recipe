import streamlit as st
import time
# App Title
st.set_page_config(page_title="Ultimate Mum-Approved Toast")

if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    loading_area = st.empty()
    
    frames = [
        "👩‍🍳 Starting the oven...",
        "🔥 Preheating...",
        "🧈 Buttering up...",
        "🥣 Mixing magic...",
        "🥚 Cracking eggs...",
        "🕒 Almost there...",
    ]
    st.caption('Your App is in the oven')
    
    for frame in frames:
        loading_area.markdown(f"### {frame}")
        time.sleep(0.7)
    
    st.session_state.loaded = True
    loading_area.empty()

# Header and Intro
st.title("Welcome to the Ultimate Mum-Approved Toast! 🧡")

st.markdown("""
Hi **Christina**! 👋

You asked for toast the recipe, and instead of just texting them like a normal person,  
I made you a tiny app, because you deserve the **crunchiest**, **butteriest** Toast ever.  
Whether you're feeding tiny humans or just need a quick snack during the chaos. 

""")

recipe = st.selectbox(
    label="Choose Recipe:",
    options=[
        "Toast",
        "Bonus Recipe: Souffle ",
    ],
    index=None,
    placeholder='Choose Recipie',
    key='recipe'
)


if recipe == "Toast":

    msg = st.toast('Gathering ingredients...')
    time.sleep(3)
    msg.toast('Mixing.. 🥣')
    time.sleep(3)
    msg.toast('Baking... 🔥')
    time.sleep(3)
    msg.toast('Toast Ready Hurray!', icon = "🍞")

    st.image('Toast.jpg')


elif recipe == "Bonus Recipe: Souffle ":
    st.markdown('''
                ### Bonus Recipe!!!
                Souffle
                 ''')
    msg = st.toast('Gathering ingredients...')
    time.sleep(3)
    msg.toast('Mixing... 🥣')
    time.sleep(3)
    msg.toast('Baking... 🔥')
    time.sleep(3)
    msg.toast('Souffle Ready Hurray!', icon = "🍮")

    st.image("Souffle.jpg")



st.caption("Made with 🧡")

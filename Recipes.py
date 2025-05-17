import streamlit as st
import time
# App Title
st.set_page_config(page_title="Ultimate Mum-Approved Toast")

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

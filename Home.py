import streamlit as st

st.set_page_config(page_title="LLTQ", layout="centered")
st.title("🎾 LOST LEGENDS: TENNIS QUEST")
st.subheader("Choose your path:")

st.page_link("pages/1_Story_Mode.py", label="⚔️ Story Mode")
st.page_link("pages/2_Padel_Mode.py", label="🔥 Padel Training")
st.page_link("pages/3_Reset_Game.py", label="🧼 Reset Game")

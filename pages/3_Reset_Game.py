import streamlit as st
import os

st.set_page_config(page_title="LLTQ - Reset Game")

st.title("🧼 Reset Game")
st.caption("This will wipe your entire LLTQ profile and all battle history.")

PLAYER_FILE = "data/player.json"
LEADERBOARD_FILE = "data/leaderboard.csv"

password = st.text_input("Password to unlock God-Mode", type="password")

if password == "vortexmaster2025":
    st.success("God-Mode unlocked.")

    if st.button("🔥 Wipe player profile"):
        if os.path.exists(PLAYER_FILE):
            os.remove(PLAYER_FILE)
            st.success("✅ Player profile deleted!")

    if st.button("🗑 Wipe leaderboard"):
        if os.path.exists(LEADERBOARD_FILE):
            os.remove(LEADERBOARD_FILE)
            st.success("✅ Leaderboard deleted!")

    if st.button("💥 Nuke EVERYTHING"):
        for f in [PLAYER_FILE, LEADERBOARD_FILE]:
            if os.path.exists(f): os.remove(f)
        st.success("☢️ Everything reset.")
else:
    st.warning("Enter correct password to enable reset options.")

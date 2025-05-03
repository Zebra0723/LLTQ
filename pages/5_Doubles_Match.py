import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(page_title="LLTQ - Multiplayer Match")

st.title("🎾 LLTQ Multiplayer Match")
st.caption("Play a 2-player duel from two separate devices.")

MATCH_FOLDER = "data/doubles_matches"
os.makedirs(MATCH_FOLDER, exist_ok=True)

# Match ID
match_id = st.text_input("Enter match code (e.g. match001)")
if not match_id:
    st.stop()

match_file = os.path.join(MATCH_FOLDER, f"{match_id}.json")

# Player info
col1, col2 = st.columns(2)
player = col1.selectbox("I am:", ["Player 1", "Player 2"])
name = col2.text_input("My Name")

rating_fields = ["Serve", "Forehand", "Backhand", "Agility", "Focus"]

ratings = {}
for stat in rating_fields:
    ratings[stat] = st.slider(f"{stat}", 1, 10, 5)

if st.button("✅ Submit My Stats"):
    if not name:
        st.error("Enter your name.")
        st.stop()

    # Load or create match file
    if os.path.exists(match_file):
        with open(match_file, "r") as f:
            match = json.load(f)
    else:
        match = {"Player 1": None, "Player 2": None, "winner": None, "timestamp": None}

    match[player] = {
        "name": name,
        "ratings": ratings
    }

    with open(match_file, "w") as f:
        json.dump(match, f)

    st.success(f"✅ {player} submitted!")

# Load and compare if both submitted
if os.path.exists(match_file):
    with open(match_file, "r") as f:
        match = json.load(f)

    p1 = match["Player 1"]
    p2 = match["Player 2"]

    if p1 and p2 and not match["winner"]:
        s1 = sum(p1["ratings"].values())
        s2 = sum(p2["ratings"].values())
        winner = p1["name"] if s1 > s2 else p2["name"] if s2 > s1 else "Tie"
        match["winner"] = winner
        match["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")

        with open(match_file, "w") as f:
            json.dump(match, f)

    if match["winner"]:
        st.markdown("---")
        st.success(f"🏆 Winner: {match['winner']}")
        st.write(f"Submitted: {match['timestamp']}")

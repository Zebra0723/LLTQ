import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="LLTQ - Quest Log")

st.title("📜 LLTQ Quest Log")
st.caption("Track your active missions across the tennis world.")

QUESTS_FILE = "data/quests.json"

# Load or init quest log
if os.path.exists(QUESTS_FILE):
    with open(QUESTS_FILE, "r") as f:
        quests = json.load(f)
else:
    quests = {
        "active": [],
        "completed": []
    }

# Sample available quests
available_quests = {
    "Beat Nadal in Paris": "🎾 Defeat the King of Clay on his home court.",
    "Find the Lost Racket in NYC": "🔍 Someone left a rare racket behind the stadium.",
    "Train 5 times in Padel Mode": "🔥 Practice hard to unlock your inner beast."
}

st.markdown("### 🆕 Available Quests")

for title, desc in available_quests.items():
    if title not in quests["active"] and title not in quests["completed"]:
        if st.button(f"🪄 Accept: {title}"):
            quests["active"].append(title)
            with open(QUESTS_FILE, "w") as f:
                json.dump(quests, f)
            st.success(f"✅ Quest '{title}' added!")
            st.experimental_rerun()
        st.caption(desc)

st.markdown("---")

# Active quests
st.markdown("### 🔄 Active Quests")
if quests["active"]:
    for quest in quests["active"]:
        st.write(f"🔸 {quest}")
else:
    st.info("No active quests.")

# Completed quests
st.markdown("### ✅ Completed Quests")
if quests["completed"]:
    for quest in quests["completed"]:
        st.write(f"✅ {quest}")
else:
    st.info("You haven’t completed any quests yet.")

# Mark as completed
if quests["active"]:
    st.markdown("---")
    st.markdown("### 🎯 Mark Quest as Completed")
    complete = st.selectbox("Which quest did you complete?", quests["active"])
    if st.button("✔️ Complete Quest"):
        quests["active"].remove(complete)
        quests["completed"].append(complete)
        with open(QUESTS_FILE, "w") as f:
            json.dump(quests, f)
        st.success(f"🏆 Quest '{complete}' completed!")
        st.experimental_rerun()

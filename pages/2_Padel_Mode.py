import streamlit as st
import json
import random
import os

st.set_page_config(page_title="LLTQ - Padel Mode")

PLAYER_FILE = "data/player.json"

# Initialize character
st.title("🔥 Padel Training Mode")
st.caption("Train your reflexes by smashing dangerous tennis balls in a padel court.")

if not os.path.exists(PLAYER_FILE):
    st.subheader("🛠️ Create your Player")
    name = st.text_input("Your Name")
    racket = st.selectbox("Choose your racket type", ["Power", "Speed", "Control"])
    if st.button("Create Player") and name:
        with open(PLAYER_FILE, "w") as f:
            json.dump({"name": name, "racket": racket}, f)
        st.success(f"Player {name} created!")
        st.experimental_rerun()
    st.stop()

with open(PLAYER_FILE, "r") as f:
    player = json.load(f)

st.subheader(f"🎾 Welcome, {player['name']} ({player['racket']} racket)")
st.markdown("---")

# Simulate incoming balls
fireballs = ["💥 Exploding Ball", "🔥 Fireball", "💣 Bomb Serve", "🌀 Spin Ghost", "💨 Speed Ball"]

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.training_log = []

st.markdown("### 🎯 Incoming Ball!")
current = random.choice(fireballs)
st.write(f"**{current} is coming at you!**")

if st.button("🎾 Return Shot"):
    hit = random.random() > 0.3
    if hit:
        st.session_state.score += 1
        st.success("✅ You hit it back!")
        st.session_state.training_log.append(f"Returned: {current}")
    else:
        st.warning("❌ Missed!")
        st.session_state.training_log.append(f"Missed: {current}")
    st.experimental_rerun()

st.markdown(f"**🔥 Total hits:** `{st.session_state.score}`")

with st.expander("📜 Training Log"):
    for log in st.session_state.training_log[::-1]:
        st.write(log)

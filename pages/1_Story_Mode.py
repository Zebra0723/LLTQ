import streamlit as st
import json
import os
import random

st.set_page_config(page_title="LLTQ - Story Mode")

PLAYER_FILE = "data/player.json"
BOSS_LIST = [
    {"name": "Novak Djokovic", "hp": 30, "attack": "laser backhand"},
    {"name": "Rafael Nadal", "hp": 35, "attack": "spin forehand"},
    {"name": "Roger Federer", "hp": 40, "attack": "floating volley"},
]

# Player check
if not os.path.exists(PLAYER_FILE):
    st.warning("🛠️ Go to Padel Mode and create your character first.")
    st.stop()

# Load player
with open(PLAYER_FILE, "r") as f:
    player = json.load(f)

st.title("⚔️ Story Mode – Boss Fight")
st.subheader(f"🎾 Player: {player['name']} ({player['racket']})")
st.markdown("---")

# Load or choose current boss
if "boss_index" not in st.session_state:
    st.session_state.boss_index = 0
    st.session_state.boss_hp = BOSS_LIST[0]["hp"]
    st.session_state.player_hp = 50
    st.session_state.log = []

boss = BOSS_LIST[st.session_state.boss_index]
st.markdown(f"### 💀 BOSS: {boss['name']}")
st.markdown(f"🧠 HP: `{st.session_state.boss_hp}`  |  💪 Your HP: `{st.session_state.player_hp}`")
st.markdown("---")

# Attacks
col1, col2 = st.columns(2)

with col1:
    if st.button("🎾 Forehand"):
        dmg = random.randint(6, 12)
        st.session_state.boss_hp -= dmg
        st.session_state.log.append(f"✅ You hit {boss['name']} for {dmg} damage!")

with col2:
    if st.button("🎾 Backhand"):
        dmg = random.randint(4, 16)
        st.session_state.boss_hp -= dmg
        st.session_state.log.append(f"✅ You hit {boss['name']} for {dmg} damage!")

# Boss turn
if random.random() < 0.6:
    dmg = random.randint(5, 10)
    st.session_state.player_hp -= dmg
    st.session_state.log.append(f"💥 {boss['name']} hits you with a {boss['attack']} for {dmg} damage!")

# Outcome
if st.session_state.boss_hp <= 0:
    st.balloons()
    st.success(f"🏆 You defeated {boss['name']}!")
    st.session_state.boss_index += 1
    if st.session_state.boss_index >= len(BOSS_LIST):
        st.success("🎉 You beat all the bosses!")
        st.stop()
    else:
        st.session_state.boss_hp = BOSS_LIST[st.session_state.boss_index]["hp"]
        st.session_state.player_hp = 50
        st.session_state.log = []
        st.experimental_rerun()

elif st.session_state.player_hp <= 0:
    st.error("💀 You were defeated. Try again.")
    st.button("🔁 Retry", on_click=lambda: st.session_state.update({
        "boss_hp": boss["hp"],
        "player_hp": 50,
        "log": []
    }))
    st.stop()

with st.expander("📜 Battle Log"):
    for entry in st.session_state.log[::-1]:
        st.write(entry)

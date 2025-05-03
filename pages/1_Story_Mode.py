import streamlit as st
import json
import random
import os

st.set_page_config(page_title="LLTQ - Story Mode")

PLAYER_FILE = "data/player.json"
BOSSES = [
    {"name": "Novak Djokovic", "hp": 30},
    {"name": "Rafael Nadal", "hp": 35},
    {"name": "Roger Federer", "hp": 40},
]

# Initialize player data
if not os.path.exists(PLAYER_FILE):
    st.warning("🛠️ Set up your character first in Padel Mode.")
    st.stop()

with open(PLAYER_FILE, "r") as f:
    player = json.load(f)

st.title("⚔️ Story Mode")
st.subheader(f"Welcome back, {player['name']}!")
st.caption(f"Your racket: {player['racket']}")
st.markdown("---")

# Pick a boss
boss = random.choice(BOSSES)
boss_hp = boss["hp"]
player_hp = 50

st.markdown(f"### 🧠 Your Mission: Defeat **{boss['name']}**")
st.markdown(f"- Boss HP: `{boss_hp}`")
st.markdown(f"- Your HP: `{player_hp}`")

# Combat system
if "damage_log" not in st.session_state:
    st.session_state.damage_log = []

if st.button("🎾 Hit with forehand"):
    dmg = random.randint(5, 12)
    boss_hp -= dmg
    st.session_state.damage_log.append(f"You hit {boss['name']} for {dmg} damage!")
if st.button("🎾 Hit with backhand"):
    dmg = random.randint(3, 15)
    boss_hp -= dmg
    st.session_state.damage_log.append(f"You hit {boss['name']} for {dmg} damage!")

# Fake boss attack
if random.random() < 0.5:
    dmg = random.randint(4, 10)
    player_hp -= dmg
    st.session_state.damage_log.append(f"{boss['name']} hit YOU for {dmg} damage!")

# Battle result
if boss_hp <= 0:
    st.success(f"🏆 YOU DEFEATED {boss['name']}!")
    st.balloons()
elif player_hp <= 0:
    st.error("💀 You were defeated. Try again.")
else:
    st.info("Battle in progress...")

# Damage log
with st.expander("📜 Combat Log"):
    for line in st.session_state.damage_log[::-1]:
        st.write(line)

import streamlit as st
import json
import os

st.set_page_config(page_title="LLTQ - World Events")

st.title("🌍 LLTQ: World Events")
st.caption("Walk the world. Talk to NPCs. Accept quests in real time.")

PLAYER_POS = "data/player_pos.json"
QUESTS_FILE = "data/quests.json"

# Grid map: name, tile, npc, quest
map_data = [
    [{"tile": "🏕️", "npc": None},
     {"tile": "🎾", "npc": "Coach Nadal", "quest": "Beat Nadal in Paris"},
     {"tile": "🏟️", "npc": None}],

    [{"tile": "🗽", "npc": "Rival", "quest": "Win a Doubles Match"},
     {"tile": "🧍", "npc": None},
     {"tile": "🗼", "npc": "Coach Federer", "quest": "Train at Paris Court"}],

    [{"tile": "🌋", "npc": None},
     {"tile": "🏖️", "npc": "Coach Serena", "quest": "Survive Padel Training"},
     {"tile": "🎯", "npc": None}]
]

# Load or create player position
if os.path.exists(PLAYER_POS):
    with open(PLAYER_POS) as f:
        pos = json.load(f)
else:
    pos = {"row": 1, "col": 1}
    with open(PLAYER_POS, "w") as f:
        json.dump(pos, f)

# Load or init quests
if os.path.exists(QUESTS_FILE):
    with open(QUESTS_FILE) as f:
        quests = json.load(f)
else:
    quests = {"active": [], "completed": []}
    with open(QUESTS_FILE, "w") as f:
        json.dump(quests, f)

# Movement buttons
def save_pos(r, c):
    with open(PLAYER_POS, "w") as f:
        json.dump({"row": r, "col": c}, f)
    st.experimental_rerun()

r, c = pos["row"], pos["col"]

col1, col2, col3 = st.columns(3)
if col2.button("⬆️ Up") and r > 0:
    save_pos(r - 1, c)
col1, col3 = st.columns(2)
if col1.button("⬅️ Left") and c > 0:
    save_pos(r, c - 1)
if col3.button("➡️ Right") and c < 2:
    save_pos(r, c + 1)
col1, col2, col3 = st.columns(3)
if col2.button("⬇️ Down") and r < 2:
    save_pos(r + 1, c)

# Display map
st.markdown("---")
for i, row in enumerate(map_data):
    cols = st.columns(len(row))
    for j, tile in enumerate(row):
        if i == r and j == c:
            cols[j].markdown("🧍")
        else:
            cols[j].markdown(tile["tile"])

# Event trigger
tile = map_data[r][c]
npc = tile.get("npc")
quest = tile.get("quest")

if npc:
    st.markdown(f"### 💬 You meet **{npc}**")

    if quest in quests["active"]:
        st.info("📝 You've already accepted this quest.")
    elif quest in quests["completed"]:
        st.success("✅ You've completed this quest.")
    else:
        st.markdown(f"**📜 Quest Available:** {quest}")
        if st.button("✅ Accept Quest"):
            quests["active"].append(quest)
            with open(QUESTS_FILE, "w") as f:
                json.dump(quests, f)
            st.success(f"Quest accepted: {quest}")

import streamlit as st

st.set_page_config(page_title="LLTQ - World Map")

st.title("🌍 LLTQ WORLD MAP")
st.caption("Walk through real-world locations and find the legends...")

# Define map grid with city labels
grid = [
    ["🗼 Paris", "   ", "🎾 Basel"],
    ["🧍", "🗽 NYC", "🏝️ Miami"],
    ["🇦🇺 Melbourne", "🏖️ Rio", "🌋 Tokyo"]
]

# Track player position
if "player_row" not in st.session_state:
    st.session_state.player_row = 1
    st.session_state.player_col = 0

# Draw map
def render_grid():
    for r, row in enumerate(grid):
        cols = st.columns(len(row))
        for c, val in enumerate(row):
            if r == st.session_state.player_row and c == st.session_state.player_col:
                cols[c].markdown("🧍 **YOU**")
            else:
                cols[c].markdown(val)

render_grid()
st.markdown("---")

# Movement buttons
c1, c2, c3 = st.columns(3)

if c2.button("⬆️ Up") and st.session_state.player_row > 0:
    st.session_state.player_row -= 1

c1, _, c3 = st.columns([1,2,1])
if c1.button("⬅️ Left") and st.session_state.player_col > 0:
    st.session_state.player_col -= 1
if c3.button("➡️ Right") and st.session_state.player_col < len(grid[0]) - 1:
    st.session_state.player_col += 1

c1, c2, c3 = st.columns(3)
if c2.button("⬇️ Down") and st.session_state.player_row < len(grid) - 1:
    st.session_state.player_row += 1

# Trigger battle
location = grid[st.session_state.player_row][st.session_state.player_col]
if "🎾" in location or "🗽" in location or "🌋" in location:
    st.success(f"You arrived at **{location.strip()}**. A challenge may appear soon...")

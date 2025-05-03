import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Reaction Dash Precision")

st.title("⚡ Reaction Dash – Precision Mode")
st.caption("Tap ONLY when the ball is in the middle target. Speed increases!")

# Game state
ss = st.session_state
ss.setdefault("pos", 0)
ss.setdefault("successes", 0)
ss.setdefault("failures", 0)
ss.setdefault("playing", False)
ss.setdefault("speed", 0.3)

# Reset
if st.button("🔄 Reset"):
    ss.pos = 0
    ss.successes = 0
    ss.failures = 0
    ss.speed = 0.3
    ss.playing = False
    st.experimental_rerun()

# Start game
if not ss.playing:
    if st.button("🎬 Start"):
        ss.playing = True
        st.experimental_rerun()
    st.stop()

# Position bar (5 slots)
bar = ["⬜"] * 5
bar[ss.pos] = "🎾"
st.markdown(" ".join(bar))

# Button
if st.button("🏓 Return Now!"):
    if ss.pos == 2:
        st.success("✅ HIT! Right on target.")
        ss.successes += 1
        ss.speed = max(0.1, ss.speed * 0.95)  # increase speed
    else:
        st.error("❌ Missed. You weren't centered!")
        ss.failures += 1
        ss.speed = min(0.5, ss.speed + 0.05)  # make easier
    ss.pos = 0

# Auto-move the ball
time.sleep(ss.speed)
ss.pos = (ss.pos + 1) % 5
st.experimental_rerun()

# Scoreboard
st.markdown("---")
st.metric("✅ Successes", ss.successes)
st.metric("❌ Misses", ss.failures)
st.metric("⚡ Speed", f"{round(1/ss.speed):.0f} moves/sec")

import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Reaction Dash")

st.title("⚡ Reaction Dash – Reflex Training")
st.caption("Wait for GO. Tap fast. Early or late = fail.")

# Init state
ss = st.session_state
ss.setdefault("phase", "idle")
ss.setdefault("successes", 0)
ss.setdefault("failures", 0)
ss.setdefault("reaction_time", None)
ss.setdefault("start_time", None)
ss.setdefault("go_signal", False)

# Reset
if st.button("🔄 Reset All"):
    for k in ["phase", "successes", "failures", "reaction_time", "start_time", "go_signal"]:
        ss.pop(k, None)
    st.experimental_rerun()

# Phase: IDLE
if ss.phase == "idle":
    st.info("Press start. Wait for GO.")
    if st.button("🎬 Start"):
        ss.phase = "waiting"
        ss.start_time = time.time() + random.uniform(2.0, 4.0)

# Phase: WAITING
elif ss.phase == "waiting":
    now = time.time()
    if now >= ss.start_time:
        ss.phase = "GO"
        ss.go_signal = True
    else:
        st.warning("⏳ Waiting... DO NOT PRESS!")
        if st.button("🏓 Too Early!"):
            ss.failures += 1
            ss.phase = "idle"
            st.error("❌ TOO EARLY!")

# Phase: GO
if ss.phase == "GO" and ss.go_signal:
    st.success("💥 GO! Tap now!")
    start_time = time.time()
    if st.button("🏓 Return Shot"):
        rt = round(time.time() - start_time, 3)
        ss.reaction_time = rt
        if rt <= 1.0:
            ss.successes += 1
            st.balloons()
            st.success(f"✅ HIT! Reaction Time: {rt}s")
        else:
            ss.failures += 1
            st.warning(f"❌ TOO SLOW ({rt}s)")
        ss.phase = "idle"
        ss.go_signal = False

# Scoreboard
st.markdown("---")
st.metric("✅ Successes", ss.successes)
st.metric("❌ Failures", ss.failures)
if ss.reaction_time is not None:
    st.metric("⚡ Last Reaction", f"{ss.reaction_time}s")

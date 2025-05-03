import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Reaction Dash")

st.title("⚡ Reaction Dash – Reflex Training")
st.caption("Wait for the GO signal. Hit return FAST. Too early or too late? You lose.")

# Initialize state
if "phase" not in st.session_state:
    st.session_state.phase = "idle"
    st.session_state.successes = 0
    st.session_state.failures = 0
    st.session_state.reaction_time = None
    st.session_state.start_time = None
    st.session_state.rerun = False

# Reset button
if st.button("🔄 Reset Training"):
    for key in ["phase", "successes", "failures", "reaction_time", "start_time", "rerun"]:
        if key in st.session_state:
            del st.session_state[key]
    st.experimental_rerun()

# Game flow
if st.session_state.phase == "idle":
    st.info("Click Start and wait for GO. Don't press early.")
    if st.button("🎬 Start"):
        st.session_state.phase = "waiting"
        st.session_state.wait_delay = random.uniform(2.0, 4.0)
        st.session_state.start_time = time.time() + st.session_state.wait_delay
        st.experimental_rerun()

elif st.session_state.phase == "waiting":
    now = time.time()
    if now >= st.session_state.start_time:
        st.session_state.phase = "GO"
        st.session_state.rerun = True  # trigger GO state rerun
    else:
        st.warning("⏳ Waiting for GO... DO NOT PRESS!")
        if st.button("🏓 Return Shot (Too Early!)"):
            st.session_state.failures += 1
            st.error("❌ TOO EARLY!")
            st.session_state.phase = "idle"

elif st.session_state.phase == "GO":
    st.success("💥 GO! HIT RETURN NOW!")
    trigger_time = time.time()
    if st.button("🏓 Return Shot"):
        reaction = round(time.time() - trigger_time, 3)
        st.session_state.reaction_time = reaction
        if reaction <= 1.0:
            st.balloons()
            st.success(f"✅ HIT! Reaction Time: {reaction} sec")
            st.session_state.successes += 1
        else:
            st.warning(f"❌ TOO SLOW. Reaction Time: {reaction} sec")
            st.session_state.failures += 1
        st.session_state.phase = "idle"

# Clean rerun (for phase switch)
if st.session_state.get("rerun"):
    del st.session_state["rerun"]
    st.experimental_rerun()

# Scoreboard
st.markdown("---")
st.metric("✅ Successes", st.session_state.successes)
st.metric("❌ Failures", st.session_state.failures)
if st.session_state.reaction_time is not None:
    st.metric("⚡ Last Reaction", f"{st.session_state.reaction_time} sec")

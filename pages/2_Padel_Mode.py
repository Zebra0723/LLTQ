import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Reaction Dash")

st.title("⚡ Reaction Dash – Reflex Training")
st.caption("Wait for the GO signal. Hit return FAST. Miss it? You lose. Hit too early? You lose.")

if "phase" not in st.session_state:
    st.session_state.phase = "idle"
    st.session_state.successes = 0
    st.session_state.failures = 0
    st.session_state.reaction_time = None
    st.session_state.challenge_ready = False
    st.session_state.start_time = None

# Reset button
if st.button("🔄 Reset Training"):
    st.session_state.phase = "idle"
    st.session_state.successes = 0
    st.session_state.failures = 0
    st.session_state.reaction_time = None
    st.session_state.challenge_ready = False
    st.session_state.start_time = None
    st.experimental_rerun()

# IDLE state
if st.session_state.phase == "idle":
    st.info("Click Start and wait for the GO signal. Don’t press early.")
    if st.button("🎬 Start"):
        st.session_state.phase = "waiting"
        st.experimental_rerun()

# WAITING state
elif st.session_state.phase == "waiting":
    delay = random.uniform(2.5, 5.0)
    st.session_state.start_time = time.time() + delay
    st.session_state.phase = "ready"
    st.experimental_rerun()

# READY state (waiting for timer to reach start)
elif st.session_state.phase == "ready":
    now = time.time()
    if now >= st.session_state.start_time:
        st.session_state.phase = "GO"
        st.experimental_rerun()
    else:
        st.warning("⏳ Waiting for GO... DO NOT PRESS!")
        if st.button("🏓 Return Shot (Too Early!)"):
            st.session_state.failures += 1
            st.error("❌ TOO EARLY!")
            st.session_state.phase = "idle"
            st.experimental_rerun()

# GO! state
elif st.session_state.phase == "GO":
    st.success("💥 GO! HIT IT NOW!")
    start = time.time()
    if st.button("🏓 Return Shot"):
        reaction = round(time.time() - start, 3)
        st.session_state.reaction_time = reaction
        if reaction <= 1.0:
            st.session_state.successes += 1
            st.balloons()
            st.success(f"✅ HIT! Reaction Time: {reaction} sec")
        else:
            st.session_state.failures += 1
            st.warning(f"❌ TOO SLOW. Time: {reaction} sec")
        st.session_state.phase = "idle"

# Stats
st.markdown("---")
st.metric("✅ Successes", st.session_state.successes)
st.metric("❌ Failures", st.session_state.failures)
if st.session_state.reaction_time is not None:
    st.metric("⚡ Last Reaction", f"{st.session_state.reaction_time} sec")

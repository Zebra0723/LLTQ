import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Real Padel Training")

st.title("🔥 Real Padel Training Mode")
st.caption("Test your reflexes! Hit the return as fast as possible when the ball appears!")

# State
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.successes = 0
    st.session_state.reaction_times = []

# Reset
if st.button("🔁 Reset Training"):
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.successes = 0
    st.session_state.reaction_times = []
    st.experimental_rerun()

# Start game
st.markdown("### Press the button AS SOON AS THE BALL APPEARS!")

if st.button("🎾 Start Round"):
    delay = random.uniform(1.5, 4.0)
    st.markdown("...Get ready...")
    time.sleep(delay)

    st.success("💥 BALL INCOMING! PRESS NOW!")
    start_time = time.time()
    pressed = st.button("🏓 Return Shot!")

    # Wait for press
    if pressed:
        rt = round(time.time() - start_time, 3)
        st.session_state.attempts += 1

        if rt < 0.3:
            st.warning("Too early! False start.")
        elif rt <= 1.0:
            st.session_state.successes += 1
            st.session_state.score += 1
            st.session_state.reaction_times.append(rt)
            st.success(f"✅ Hit! Reaction time: {rt} sec")
        else:
            st.warning(f"❌ Too slow. Reaction time: {rt} sec")

# Summary
st.markdown("---")
st.markdown(f"🏅 Score: `{st.session_state.score}`")
st.markdown(f"✅ Successes: `{st.session_state.successes}` / Attempts: `{st.session_state.attempts}`")

if st.session_state.reaction_times:
    avg_rt = round(sum(st.session_state.reaction_times) / len(st.session_state.reaction_times), 3)
    st.markdown(f"⚡ Average Reaction Time: `{avg_rt} sec`")

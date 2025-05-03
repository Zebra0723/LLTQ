import streamlit as st
import time
import random

st.set_page_config(page_title="LLTQ - Padel Mode")

st.title("🔥 Real Padel Training Mode")
st.caption("Choose a skill challenge. These are REAL tennis drills, not button spam.")

# State initialization
if "padel_score" not in st.session_state:
    st.session_state.padel_score = 0
    st.session_state.padel_streak = 0
    st.session_state.padel_combo = []

st.markdown("### 🎮 Choose your Training Mode")
mode = st.radio("", ["🎯 Target Drill", "⏱️ Timed Rally", "🧠 Pattern Memory"])

st.markdown("---")

# 🎯 TARGET DRILL
if mode == "🎯 Target Drill":
    st.subheader("🎯 Hit only when the ball is GREEN (🟢)")

    if "target_ball" not in st.session_state:
        st.session_state.target_ball = random.choice(["🔴", "🟡", "🟢", "🔴", "🟢"])

    if st.button("🎾 Reveal Ball"):
        st.session_state.show_target = True

    if st.session_state.get("show_target", False):
        st.markdown(f"**Ball: {st.session_state.target_ball}**")
        if st.button("🏓 Hit"):
            if st.session_state.target_ball == "🟢":
                st.success("✅ Nice shot!")
                st.session_state.padel_score += 1
                st.session_state.padel_streak += 1
            else:
                st.error("❌ Missed! Wrong ball.")
                st.session_state.padel_streak = 0
            del st.session_state.target_ball
            del st.session_state.show_target

# ⏱️ TIMED RALLY
elif mode == "⏱️ Timed Rally":
    st.subheader("⏱️ Hit 3 shots as FAST as you can")

    if st.button("🎬 Start Rally"):
        st.session_state.rally_start = time.time()
        st.session_state.rally_hits = 0
        st.session_state.rally_required = 3
        st.session_state.rally_done = False

    if st.session_state.get("rally_start") and not st.session_state.get("rally_done"):
        if st.button("🏓 Rally Hit"):
            st.session_state.rally_hits += 1
            if st.session_state.rally_hits >= st.session_state.rally_required:
                elapsed = round(time.time() - st.session_state.rally_start, 2)
                st.success(f"✅ 3 shots in {elapsed} seconds!")
                st.session_state.padel_score += 1
                st.session_state.padel_streak += 1
                st.session_state.rally_done = True

# 🧠 PATTERN MEMORY
elif mode == "🧠 Pattern Memory":
    st.subheader("🧠 Repeat the combo: Serve → Forehand → Backhand")

    if st.button("👁 Show Pattern"):
        st.session_state.padel_combo = ["Serve", "Forehand", "Backhand"]
        st.session_state.padel_input = []

    if st.session_state.get("padel_combo"):
        col1, col2, col3 = st.columns(3)
        if col1.button("Serve"):
            st.session_state.padel_input.append("Serve")
        if col2.button("Forehand"):
            st.session_state.padel_input.append("Forehand")
        if col3.button("Backhand"):
            st.session_state.padel_input.append("Backhand")

        if len(st.session_state.padel_input) == len(st.session_state.padel_combo):
            if st.session_state.padel_input == st.session_state.padel_combo:
                st.success("✅ Combo complete!")
                st.session_state.padel_score += 1
                st.session_state.padel_streak += 1
            else:
                st.error("❌ Incorrect pattern!")
                st.session_state.padel_streak = 0
            del st.session_state.padel_combo
            del st.session_state.padel_input

# Display stats
st.markdown("---")
st.metric("🏅 Total Score", st.session_state.padel_score)
st.metric("🔥 Current Streak", st.session_state.padel_streak)

if st.button("🔄 Reset Training"):
    st.session_state.padel_score = 0
    st.session_state.padel_streak = 0
    st.session_state.padel_combo = []
    st.experimental_rerun()

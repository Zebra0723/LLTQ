import streamlit as st
import random
from datetime import datetime
import pandas as pd
import os

st.set_page_config(page_title="LLTQ - Doubles Mode")
st.title("🎾 Doubles Mode – Player vs Player")
st.caption("Rate your way to victory. First to break wins!")

file = "data/doubles_leaderboard.csv"
if not os.path.exists(file):
    pd.DataFrame(columns=["Time", "Player 1", "Player 2", "Winner", "Score 1", "Score 2"]).to_csv(file, index=False)

# Player setup
col1, col2 = st.columns(2)
player1 = col1.text_input("🧑 Player 1 Name", key="p1")
player2 = col2.text_input("🧑 Player 2 Name", key="p2")

rating_fields = ["Serve", "Forehand", "Backhand", "Agility", "Mental Strength"]

if not player1 or not player2 or player1 == player2:
    st.warning("Enter two different player names to start.")
    st.stop()

st.markdown("---")
st.subheader("🎯 Rate Each Player")

score1, score2 = {}, {}

for stat in rating_fields:
    c1, c2 = st.columns(2)
    score1[stat] = c1.slider(f"{stat} – {player1}", 1, 10, 5)
    score2[stat] = c2.slider(f"{stat} – {player2}", 1, 10, 5)

# Submission
if st.button("🏆 Submit Duel"):
    total1 = sum(score1.values())
    total2 = sum(score2.values())

    winner = player1 if total1 > total2 else player2 if total2 > total1 else "Tie"

    df = pd.read_csv(file)
    row = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Player 1": player1,
        "Player 2": player2,
        "Winner": winner,
        "Score 1": total1,
        "Score 2": total2
    }
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(file, index=False)

    st.success(f"🎉 Winner: {winner}!")
    st.balloons()

# Leaderboard
st.markdown("---")
st.subheader("📈 Doubles Leaderboard (Latest)")
df = pd.read_csv(file)
st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)

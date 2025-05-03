st.title("🔥 Real Padel Training")

mode = st.radio("Choose training mode:", ["🎯 Target Drill", "⏱️ Timed Rally", "🧠 Pattern Match"])

if mode == "🎯 Target Drill":
    # Launch emoji targets, hit green only
elif mode == "⏱️ Timed Rally":
    # Hit X targets under Y seconds
elif mode == "🧠 Pattern Match":
    # Show combo, player must repeat correctly

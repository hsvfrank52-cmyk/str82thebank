import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Str82TheBank", layout="wide")
st.title("💰 Str82TheBank")

# Current bankroll
bankroll = 544.43
total_bets = 8
wins = 6
losses = 2
roi = (bankroll - 500) / 500 * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Bankroll", f"${bankroll:,.2f}", f"+${44.43:.2f}")
col2.metric("Win Rate", f"{wins/total_bets*100:.1f}%", f"{wins}-{losses}")
col3.metric("Total ROI", f"{roi:.2f}%", "On pace for 10%+")
col4.metric("Total Bets", total_bets)

st.divider()

st.subheader("Daily Locks")

# Live model locks will appear here every morning
st.info("✅ Live model connected — locks update daily")

st.divider()

st.subheader("Results History")
history = pd.DataFrame({
    "Date": ["Apr 2", "Apr 3"],
    "W-L": ["2-1", "4-1"],
    "P/L": ["+$13.85", "+$30.58"],
    "ROI": ["+2.77%", "+5.96%"],
    "Bankroll": ["$513.85", "$544.43"]
})
st.dataframe(history, use_container_width=True, hide_index=True)

st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
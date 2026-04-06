import streamlit as st
import pandas as pd
from datetime import datetime

# Exact dark theme from your screenshots
st.set_page_config(page_title="Str82TheBank", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .big-font { font-size: 52px !important; font-weight: bold; color: #FFFFFF; }
    .green-text { color: #00FF7F; }
    .metric-label { font-size: 14px; color: #AAAAAA; }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 STR82THEBANK")
st.caption("LIVE • 24/7 BASEBALL • 1-4% DISCIPLINE")

# Bankroll section (exact style from your screenshots)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="big-font">$526.33</p>', unsafe_allow_html=True)
    st.markdown('<span class="green-text">+$26.33 P/L</span> &nbsp;&nbsp;&nbsp; <span class="green-text">+5.27% ROI</span>', unsafe_allow_html=True)

st.markdown("**13 - 10 - 0** RECORD", unsafe_allow_html=True)

# Win rate bar
st.progress(0.565)
st.caption("56.5% WIN RATE")

st.divider()

st.subheader("Daily Locks")

locks_data = [
    {"Sport": "MLB", "Game": "Phillies @ Mets (12:10 PM CT)", "Pick": "Phillies ML", "Best Price": "-132", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Dodgers @ Nationals (12:35 PM CT)", "Pick": "Dodgers ML", "Best Price": "-138", "Stars": "4", "Stake": "$16"},
    {"Sport": "MLB", "Game": "Yankees vs Marlins (12:35 PM CT)", "Pick": "Yankees ML", "Best Price": "-145", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Red Sox vs Padres (12:35 PM CT)", "Pick": "Red Sox ML", "Best Price": "-118", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Astros @ Athletics (8:05 PM CT)", "Pick": "Astros ML", "Best Price": "-135", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Guardians @ Twins (1:10 PM CT)", "Pick": "Twins ML", "Best Price": "+110", "Stars": "3", "Stake": "$11"}
]
df_locks = pd.DataFrame(locks_data)
st.dataframe(df_locks, use_container_width=True, hide_index=True)

# Rollover Lock highlight
st.subheader("🔥 ROLLOVER LOCK OF THE DAY")
st.success("**Dodgers ML @ -138** (4 stars, 89% confidence)\n\nThis is the single best compounding opportunity today.")
st.divider()

# Real April 2026 calendar with corrected April 5 results
st.subheader("April 2026")
calendar_data = pd.DataFrame({
    "Date": ["2", "3", "4", "5"],
    "P/L": ["+$13.85", "+$30.58", "+$4.30", "–$22.40"],
    "Record": ["2-1", "4-1", "3-2", "4-6"]
})
st.dataframe(calendar_data, use_container_width=True, hide_index=True)

st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
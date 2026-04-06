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
st.caption("• 24/7 BASEBALL • 1-4% DISCIPLINE")

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
    {"Sport": "MLB", "Game": "Cubs @ Rays (3:10 PM CT)", "Pick": "Rays ML", "Best Price": "-128", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Royals @ Guardians (5:10 PM CT)", "Pick": "Guardians ML", "Best Price": "-132", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Padres @ Pirates (5:40 PM CT)", "Pick": "Pirates ML", "Best Price": "-120", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Astros @ Rockies (7:40 PM CT)", "Pick": "Astros ML", "Best Price": "-138", "Stars": "4", "Stake": "$16"},
    {"Sport": "MLB", "Game": "Braves @ Angels (8:38 PM CT)", "Pick": "Braves ML", "Best Price": "-130", "Stars": "3", "Stake": "$11"},
    {"Sport": "MLB", "Game": "Phillies @ Giants (8:45 PM CT)", "Pick": "Phillies ML", "Best Price": "-125", "Stars": "3", "Stake": "$11"}
]
df_locks = pd.DataFrame(locks_data)
st.dataframe(df_locks, use_container_width=True, hide_index=True)

st.subheader("🔥 ROLLOVER LOCK OF THE DAY")
st.success("**Astros ML @ -138** (4 stars, 89% confidence)\n\nThis is the single best compounding opportunity today.")
# Real April 2026 calendar with corrected April 5 results
st.subheader("April 2026")
calendar_data = pd.DataFrame({
    "Date": ["2", "3", "4", "5"],
    "P/L": ["+$13.85", "+$30.58", "+$4.30", "–$22.40"],
    "Record": ["2-1", "4-1", "3-2", "4-6"]
})
st.dataframe(calendar_data, use_container_width=True, hide_index=True)

st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
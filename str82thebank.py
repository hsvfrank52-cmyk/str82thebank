import streamlit as st
import pandas as pd
from datetime import datetime

# Dark theme matching your screenshots
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

# Bankroll section (matches your screenshot)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="big-font">$548.73</p>', unsafe_allow_html=True)
    st.markdown('<span class="green-text">+$48.73 P/L</span> &nbsp;&nbsp;&nbsp; <span class="green-text">+9.75% ROI</span>', unsafe_allow_html=True)

st.markdown("**21 - 5 - 0** RECORD", unsafe_allow_html=True)

# Win rate bar
st.progress(0.692)  # 69.2% from current record
st.caption("69.2% WIN RATE")

st.divider()

# Locks section
st.subheader("🔒 LOCKS")
st.info("No locks today — model will auto-populate at 10:00 AM CT")

st.divider()

# April 2026 Calendar (exactly like your screenshot)
st.subheader("April 2026")
calendar_data = pd.DataFrame({
    "Date": ["1", "2", "3", "4", "5"],
    "P/L": ["+$535", "+$489", "+$621", "+$471", "—"],
    "Record": ["5-1", "3-0", "6-2", "7-2", "—"]
})
st.dataframe(calendar_data, use_container_width=True, hide_index=True)

st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")

st.success("✅ Dashboard now matches your screenshots")
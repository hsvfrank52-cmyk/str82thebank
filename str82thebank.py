import streamlit as st
import pandas as pd
from datetime import datetime

# Dark theme exactly like your screenshots
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

# Bankroll section (matches your screenshot style)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="big-font">$548.73</p>', unsafe_allow_html=True)
    st.markdown('<span class="green-text">+$48.73 P/L</span> &nbsp;&nbsp;&nbsp; <span class="green-text">+9.75% ROI</span>', unsafe_allow_html=True)

st.markdown("**9 - 4 - 0** RECORD", unsafe_allow_html=True)

# Win rate bar
st.progress(0.692)
st.caption("69.2% WIN RATE")

st.divider()

# Locks section
st.subheader("🔒 LOCKS")
st.info("No locks today — model will auto-populate at 10:00 AM CT")

st.divider()

# April 2026 Calendar (real data only)
st.subheader("April 2026")
calendar_data = pd.DataFrame({
    "Date": ["2", "3", "4", "5"],
    "P/L": ["+$13.85", "+$30.58", "+$4.30", "—"],
    "Record": ["2-1", "4-1", "3-2", "Pending"]
})
st.dataframe(calendar_data, use_container_width=True, hide_index=True)

st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")
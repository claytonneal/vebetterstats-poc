import pandas as pd
import streamlit as st

from loader import get_round_numbers, load_round_data
from stats import RoundStats
from ui import render_app_cards

# create title
st.title("VeBetterStats")
st.caption("Stats and analytics for VeBetter rounds")

# get available rounds data
round_numbers = get_round_numbers()

# allow user to select the round
selected_round = st.selectbox(
    "Select round",
    round_numbers,
    index=len(round_numbers) - 1 if round_numbers else None,
)
if selected_round is None:
    st.warning("No rounds available.")
    st.stop()
st.divider()


# load round data
df = load_round_data(int(selected_round))
# init stats
stats = RoundStats(df)
round_summary = stats.get_round_summary()

# display round summary
st.subheader("Round Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Actions", round_summary.total_actions)
col2.metric("Unique Users", round_summary.total_unique_users)
col3.metric("B3TR Rewarded", f"{round_summary.total_b3tr:,.2f}")
st.divider()

# display app summaries
st.subheader("Apps Summary")
app_summary = stats.get_apps_summary()
df_stats = app_summary.sort_values("total_actions", ascending=False).reset_index(
    drop=True
)
render_app_cards(df_stats)

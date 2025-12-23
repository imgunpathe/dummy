import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tyre Production IIoT Dashboard",
    layout="wide"
)

kpi = pd.read_csv("summary_kpi.csv")
shift_summary = pd.read_csv("shift_summary.csv")

st.title("Motorcycle Tyre Production – Full OEE & Energy Analytics")

# -------------------------------------------------
# KPI SECTION
# -------------------------------------------------

cols = st.columns(5)

for col, (_, row) in zip(cols, kpi.iterrows()):
    col.metric(row["metric"], row["value"])

# -------------------------------------------------
# SHIFT-WISE ENERGY & QUALITY
# -------------------------------------------------

st.subheader("Shift-wise Energy Efficiency")

energy_chart = shift_summary.set_index("shift")["energy_per_tyre"]
st.bar_chart(energy_chart)

st.subheader("Shift-wise Production Summary")
st.dataframe(shift_summary)

# -------------------------------------------------
# MANAGEMENT INSIGHT
# -------------------------------------------------

worst_shift = shift_summary.sort_values(
    "energy_per_tyre", ascending=False
).iloc[0]["shift"]

st.warning(
    f"⚠️ Highest energy consumption per tyre observed in **{worst_shift}**. "
    "Investigate process stability and operator practices in this shift."
)

import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("🔍 Device Analytics")

device = st.selectbox(
    "Select Device Type",
    df['Device_Type'].unique()
)

filtered = df[df['Device_Type'] == device]

# KPI
st.metric(
    "Total Devices",
    len(filtered)
)

# MANUFACTURER PIE CHART
fig1 = px.pie(
    filtered,
    names="Manufacturer",
    title="Manufacturer Distribution"
)


st.plotly_chart(fig2, use_container_width=True)

# DOWNTIME HISTOGRAM
fig3 = px.histogram(
    filtered,
    x="Downtime",
    nbins=30,
    color_discrete_sequence=['red']
)

st.plotly_chart(fig3, use_container_width=True)

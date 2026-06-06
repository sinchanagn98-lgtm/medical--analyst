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
# --------------------------------
# CLEAN DATA
# --------------------------------

filtered["Failure_Event_Count"] = pd.to_numeric(
    filtered["Failure_Event_Count"],
    errors="coerce"
)

filtered["Downtime"] = pd.to_numeric(
    filtered["Downtime"],
    errors="coerce"
)

filtered["Maintenance_Cost"] = pd.to_numeric(
    filtered["Maintenance_Cost"],
    errors="coerce"
)

# Remove invalid rows
scatter_df = filtered.dropna(
    subset=[
        "Failure_Event_Count",
        "Downtime",
        "Maintenance_Cost"
    ]
)

# Remove invalid bubble sizes
scatter_df = scatter_df[
    scatter_df["Maintenance_Cost"] > 0
]

# --------------------------------
# SAFE SCATTER PLOT
# --------------------------------

fig2 = px.scatter(
    scatter_df,
    x="Failure_Event_Count",
    y="Downtime",
    size="Maintenance_Cost",
    color="Country",
    hover_data=["Manufacturer"],
    title="Failure Events vs Downtime"
)

st.plotly_chart(
    fig2,
    use_container_width=True,
    key="device_scatter_chart"
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

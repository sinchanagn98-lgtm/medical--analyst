
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

st.title("📊 Dashboard")

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Devices",
    len(df)
)

col2.metric(
    "Total Maintenance Cost",
    f"${df['Maintenance_Cost'].sum():,.0f}"
)

col3.metric(
    "Average Downtime",
    f"{df['Downtime'].mean():.2f} hrs"
)

col4.metric(
    "Total Failure Events",
    int(df['Failure_Event_Count'].sum())
)

st.divider()

# DEVICE TYPE DISTRIBUTION
st.subheader("Device Type Distribution")

fig1 = px.bar(
    x=df['Device_Type'].value_counts().index,
    y=df['Device_Type'].value_counts().values,
    color=df['Device_Type'].value_counts().index
)

st.plotly_chart(fig1, use_container_width=True)

# MAINTENANCE COST ANALYSIS
st.subheader("Maintenance Cost Analysis")

fig2 = px.box(
    df,
    x="Device_Type",
    y="Maintenance_Cost",
    color="Device_Type"
)

st.plotly_chart(fig2, use_container_width=True)

# AGE VS DOWNTIME
st.subheader("Age vs Downtime")
# --------------------------------
# CLEAN DATA FOR SCATTER PLOT
# --------------------------------

# Convert columns to numeric
df["Failure_Event_Count"] = pd.to_numeric(
    df["Failure_Event_Count"],
    errors="coerce"
)

df["Downtime"] = pd.to_numeric(
    df["Downtime"],
    errors="coerce"
)

df["Maintenance_Cost"] = pd.to_numeric(
    df["Maintenance_Cost"],
    errors="coerce"
)

# Remove invalid rows
scatter_df = df.dropna(
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

fig3 = px.scatter(
    scatter_df,
    x="Failure_Event_Count",
    y="Downtime",
    size="Maintenance_Cost",
    color="Country",
    hover_data=["Device_Type"],
    title="Failure Events vs Downtime"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


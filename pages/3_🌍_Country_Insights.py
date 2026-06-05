import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("🌍 Country Insights")

# COUNTRY COST
country_cost = df.groupby(
    "Country"
)["Maintenance_Cost"].sum().reset_index()

fig1 = px.choropleth(
    country_cost,
    locations="Country",
    locationmode="country names",
    color="Maintenance_Cost",
    title="Maintenance Cost by Country"
)

st.plotly_chart(fig1, use_container_width=True)

# FAILURE EVENTS
country_failure = df.groupby(
    "Country"
)["Failure_Event_Count"].sum().reset_index()

fig2 = px.bar(
    country_failure,
    x="Country",
    y="Failure_Event_Count",
    color="Failure_Event_Count"
)

st.plotly_chart(fig2, use_container_width=True)

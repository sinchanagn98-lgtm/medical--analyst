import streamlit as st

st.set_page_config(
    page_title="Medical Equipment Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Equipment Maintenance Tracker")
st.markdown("""
### Predictive Maintenance & Deep Analytics Platform

Monitor:
- Device Failures
- Maintenance Cost
- Downtime
- Device Health
- Country Insights
- Predictive Analytics
""")

st.image("assets/banner.jpg", use_container_width=True)

st.success("Use the sidebar to navigate through analytics pages.")

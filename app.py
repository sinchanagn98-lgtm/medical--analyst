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

st.markdown("""
<div style="
    background: linear-gradient(90deg,#0f172a,#1e40af);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
">

<h1>🏥 Medical Device Failure Analytics</h1>

<h3>Advanced Healthcare Monitoring Dashboard</h3>

<p>
📊 Deep Analytics |
🌍 Global Insights |
⚠️ Failure Prediction |
🧠 Smart Monitoring
</p>

</div>
""", unsafe_allow_html=True)

st.success("Use the sidebar to navigate through analytics pages.")

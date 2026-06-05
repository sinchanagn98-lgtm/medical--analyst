import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from utils.data_loader import load_data

df = load_data()

st.title("📈 Advanced Charts")

# SUNBURST CHART
fig1 = px.sunburst(
    df,
    path=['Country', 'Device_Type', 'Manufacturer'],
    values='Maintenance_Cost'
)

st.plotly_chart(fig1, use_container_width=True)

# TREEMAP
fig2 = px.treemap(
    df,
    path=['Device_Type', 'Manufacturer'],
    values='Failure_Event_Count'
)

st.plotly_chart(fig2, use_container_width=True)

# WORD CLOUD
if 'Maintenance_Report' in df.columns:

    text = " ".join(
        df['Maintenance_Report'].astype(str)
    )

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.imshow(wordcloud)

    ax.axis("off")

    st.pyplot(fig)

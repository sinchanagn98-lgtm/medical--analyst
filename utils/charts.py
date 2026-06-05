import plotly.express as px

def device_chart(df):

    fig = px.bar(
        x=df['Device_Type'].value_counts().index,
        y=df['Device_Type'].value_counts().values
    )

    return fig

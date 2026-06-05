def generate_insights(df):

    top_device = df['Device_Type'].value_counts().idxmax()

    high_cost_country = df.groupby(
        'Country'
    )['Maintenance_Cost'].sum().idxmax()

    insight = f"""
    Most used device: {top_device}

    Highest maintenance spending country:
    {high_cost_country}
    """

    return insight

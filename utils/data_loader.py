import pandas as pd

def load_data():

    df = pd.read_csv(
        "dataset/Medical_Device_Failure_dataset.csv"
    )

    # Convert date column
    if 'Purchase_Date' in df.columns:
        df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])

    return df

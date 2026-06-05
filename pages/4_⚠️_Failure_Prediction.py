import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = load_data()

st.title("⚠️ Failure Prediction")

features = [
    'Age',
    'Maintenance_Cost',
    'Downtime',
    'Maintenance_Frequency'
]

X = df[features]
y = df['Maintenance_Class']

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestClassifier()

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

st.success(
    f"Model Accuracy: {accuracy*100:.2f}%"
)

# USER INPUTS
st.subheader("Predict Maintenance Class")

age = st.slider(
    "Device Age",
    1,
    20,
    5
)

cost = st.number_input(
    "Maintenance Cost",
    1000,
    100000,
    5000
)

downtime = st.slider(
    "Downtime",
    1,
    100,
    10
)

frequency = st.slider(
    "Maintenance Frequency",
    1,
    20,
    5
)

sample = pd.DataFrame({
    'Age': [age],
    'Maintenance_Cost': [cost],
    'Downtime': [downtime],
    'Maintenance_Frequency': [frequency]
})

prediction = model.predict(sample)

st.warning(
    f"Predicted Maintenance Class: {prediction[0]}"
)

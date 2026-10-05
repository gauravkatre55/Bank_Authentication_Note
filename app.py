import streamlit as st
import joblib
import numpy as np

# Load trained model
classifier = joblib.load("classifier.pkl")

st.set_page_config(
    page_title="Bank Note Authentication",
    page_icon="💵"
)

st.title("💵 Bank Note Authentication")

st.write(
    "Enter the four features to predict whether the banknote is genuine or fake."
)

variance = st.number_input(
    "Variance",
    value=0.0
)

skewness = st.number_input(
    "Skewness",
    value=0.0
)

curtosis = st.number_input(
    "Curtosis",
    value=0.0
)

entropy = st.number_input(
    "Entropy",
    value=0.0
)

if st.button("Predict"):

    input_data = np.array([
        [variance, skewness, curtosis, entropy]
    ])

    prediction = classifier.predict(input_data)

    st.write("Prediction:", prediction[0])

    if prediction[0] == 0:
        st.success("Genuine Banknote")
    else:
        st.error("Fake Banknote")
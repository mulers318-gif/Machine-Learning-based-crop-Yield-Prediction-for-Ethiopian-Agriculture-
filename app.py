import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(
    open("crop_yield_model.pkl","rb")
)

# Load encoders
region_encoder = pickle.load(
    open("region_encoder.pkl","rb")
)

crop_encoder = pickle.load(
    open("crop_encoder.pkl","rb")
)

st.title(
    "Ethiopian Crop Yield Prediction"
)

year = st.number_input(
    "Year",
    value=2027
)

region = st.selectbox(
    "Region",
    region_encoder.classes_
)

crop = st.selectbox(
    "Crop Type",
    crop_encoder.classes_
)

area = st.number_input(
    "Area Cultivated (Ha)"
)

production = st.number_input(
    "Production (Kg)"
)

if st.button("Predict Yield"):

    region_code = region_encoder.transform(
        [region]
    )[0]

    crop_code = crop_encoder.transform(
        [crop]
    )[0]

    data = pd.DataFrame({

        "Year":[year],

        "Region":[region_code],

        "crop_type":[crop_code],

        "Area_cultivatedHa":[area],

        "Productionkg":[production]

    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Yield: {prediction[0]:.2f} kg/ha"
    )
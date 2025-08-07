import pandas as pd
import numpy as np
import joblib  
import streamlit as st
import os
import joblib
model = joblib.load('oxoxgcarmodel.pkl')

st.title('🚗 Car Price Prediction ML App')

# Load the dataset
@st.cache_data
def load_data():
    data_path = os.path.join(os.getcwd(), 'realcar.csv')
    return pd.read_csv(data_path)

cars_data = load_data()

# Extract brand name from full car name
def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

# UI Elements
name = st.selectbox('Select Car Brand', sorted(cars_data['name'].unique()))
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('KMs Driven', 11, 200000)
seats = int(st.selectbox('Number of Seats', [4, 5, 6, 7, 8, 9, 10, 14]))

fuel = st.selectbox('Fuel Type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller Type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', cars_data['transmission'].unique())
owner = st.selectbox('Ownership', cars_data['owner'].unique())
mileage = st.slider('Mileage (kmpl)', 10, 40)
engine = st.slider('Engine (CC)', 700, 5000)
max_power = st.slider('Max Power (BHP)', 0, 300)

# Predict button
if st.button("Predict Price"):
    # Prepare input
    input_df = pd.DataFrame([[name, year, km_driven, fuel, seller_type, transmission,
                              owner, mileage, engine, max_power, seats]],
                            columns=['name', 'year', 'km_driven', 'fuel', 'seller_type',
                                     'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])

    # Encode categorical variables
    input_df['owner'].replace(
        ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'],
        [1, 2, 3, 4, 5], inplace=True)

    input_df['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)

    input_df['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)

    input_df['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)

    input_df['name'].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
         'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
         'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
         'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
         'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
        list(range(1, 32)), inplace=True)

    # Predict and display
    prediction = model.predict(input_df)
    st.success(f"💰 Estimated Car Price: ₹ {prediction[0]:,.2f}")


# 🚗 Car Price Prediction Web App

This is a Streamlit-based web application that predicts the resale price of a car based on various features such as brand, year, fuel type, kilometers driven, etc. It uses a machine learning model trained with XGBoost and scikit-learn.

## 🛠 Features

Predicts price based on:
- Car brand  
- Year of manufacture  
- KMs driven  
- Fuel type  
- Seller type  
- Transmission  
- Ownership  
- Mileage  
- Engine  
- Max power  
- Seats  

Additional:
- Clean, simple UI using Streamlit  
- Interactive sliders and dropdowns for user inputs  
- Model trained on real car dataset  

## 📁 Files Included

- `app.py` – Streamlit app script  
- `finalcar_project.ipynb` – Notebook for training and saving the model  
- `oxoxgcarmodel.pkl` – Saved ML model (using `joblib`)  
- `realcar.csv` – Dataset used for model and dropdown values  
- `requirements.txt` – List of dependencies for deployment  

## 🧠 Model Details

- **Algorithm:** XGBoost Regressor  
- **Encoding:** Manual integer encoding of categorical values  
- **Training Notebook:** `finalcar_project.ipynb`  

## 🚀 How to Use (Streamlit Cloud)

1. Go to the deployed app: https://carpredictionmodelxg-25.streamlit.app/
2. Fill in the car details  
3. Click on **Predict**  
4. See the estimated resale price instantly!  

## 🙌 Acknowledgements

- Dataset sourced from Kaggle and cleaned for training  
- UI powered by Streamlit  
- Machine Learning model created using XGBoost  

## 👤 Author

**Prajwal** — *Machine Learning & Python Developer*



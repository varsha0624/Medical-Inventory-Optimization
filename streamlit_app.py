import pandas as pd
import streamlit as st
import numpy as np
import pickle
from datetime import datetime


# Load the model
try:
    with open(r"E:\Project\forecast_model_double_exp.pickle", 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error('Model file not found. Please run the training script first.')
    st.stop()

# Define a function to take user input and make prediction
def predict_quantity(date):
    # Convert date string to datetime object
    date = datetime.strptime(date, '%Y-%m-%d')
    # Create a pandas Timestamp object
    date = pd.Timestamp(date)
    # Make a prediction using the loaded model
    prediction = model.predict(start=date, end=date)[0]
    return prediction

# Create a Streamlit app
st.set_page_config(page_title='Medicine Demand Forecasting App', page_icon=':pill:', layout='wide', initial_sidebar_state='collapsed')
st.title('Medicine Demand Forecasting App')

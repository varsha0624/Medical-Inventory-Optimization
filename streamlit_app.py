import pandas as pd
import streamlit as st
import numpy as np
import pickle
from datetime import datetime

# Load the model
try:
    with open(r"C:\Users\Varsh\model.pickle", 'rb') as f:
        model = pickle.load(f)
 

# Define a function to take user input and make prediction
defpredict_quantity(date):
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

# Add a date input widget
date = st.date_input('Enter a date')

# Make a prediction when the user clicks the "Predict" button
if st.button('Predict'):
    prediction = predict_quantity(str(date))
    st.success(f'The predicted quantity for {date} is {prediction}.')
    # Add a chart with the predicted quantity
    dates = pd.date_range(start=date, end=date)
    quantities = [prediction]
    df = pd.DataFrame({'Quantity': quantities}, index=dates)
    st.line_chart(df, use_container_width=True)
else:
    st.info('Click the "Predict" button to make a prediction.')

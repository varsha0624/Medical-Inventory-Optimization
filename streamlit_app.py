import pandas as pd
import streamlit as st
import numpy as np
import pickle
from datetime import datetime


# Load the model
model = pickle.load(open("E:\Project\forecast_model_double_exp.pickle",'wb'))

#load dataset to plot alongside predictions
df = pd.read_csv("E:\Project\DayForecast.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index(['Date'], inplace=True)

#page configuration
st.set_page_config(layout='centered')
image = Image.open("F:\Model Depolyment\drug _image.jpg")
st.image(image)

date = st.slider("Select number of dates",1,30,step = 1)
    
    
pred = model.forecast(date)
pred = pd.DataFrame(pred, columns=['Quantity'])
   
if st.button("Predict"):

        col1, col2 = st.columns([2,3])
        with col1:
             st.dataframe(pred)
        with col2:
            fig, ax = plt.subplots()
            df['Quantity'].plot(style='--', color='gray', legend=True, label='known')
            pred['Quantity'].plot(color='b', legend=True, label='prediction')
            st.pyplot(fig)

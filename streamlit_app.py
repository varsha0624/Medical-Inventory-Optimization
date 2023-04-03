import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
import base64
from statsmodels.tsa.arima.model import ARIMAResults

hide_st_style = """
           <style>
            MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:before{
                content: "It is a Time Series(ARIMA) Model with overall accuracy of 98%"; 
                display: block;
                position: relative;
                color: black;
                }
            footer:after{
                content: "Built by Pragya."; 
                display: block;
                position: relative;
                color: black;
                }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# BACKGROUND IMAGE
def add_bg_from_local(photo):
    with open(photo, "rb") as photo:
        encoded_string = base64.b64encode(photo.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True)
add_bg_from_local('pharmacy.jpg')

st.markdown("""
<style>
div[data-baseweb="select"] > div {
    background-color: #A4DCC5;
    width: 600px;
}
</style>""", unsafe_allow_html=True)

st.title("Pharma Sales Forecasting")

data = pickle.load(open("data.pkl","rb"))
model_NORADRENALINE= ARIMAResults.load('models\model_NORADRENALINE.pkl')
model_LEVOSALBUTAMOL= ARIMAResults.load('models\LEVOSALBUTAMOL.pkl')
model_ONDANSETRON= ARIMAResults.load('models\ONDANSETRON.pkl')
model_PANTOPRAZOLE= ARIMAResults.load('models\PANTOPRAZOLE.pkl')
model_MULTIPLE_ELECTROLYTES= ARIMAResults.load('models\MULTIPLE_ELECTROLYTES.pkl')
model_PARACETAMOL= ARIMAResults.load('models\PARACETAMOL.pkl')
model_SEVOFLURANE= ARIMAResults.load('models\SEVOFLURANE.pkl')
model_SODIUM_CHLORIDE_IVF= ARIMAResults.load('models\SODIUM_CHLORIDE_IVF.pkl')
model_SODIUM_CHLORIDE= ARIMAResults.load('models\SODIUM_CHLORIDE.pkl')
model_WATER_FOR_INJECTION= ARIMAResults.load('models\WATER_FOR_INJECTION.pkl')

Brand= ['SEVOFLURANE 99.97%', 'NORADRENALINE 2ML INJ',
       'LEVOSALBUTAMOL/LEVALBUTEROL 0.63MG RESPULES',
       'WATER FOR INJECTION 10ML SOLUTION', 'PARACETAMOL 1GM IV INJ',
       'SODIUM CHLORIDE IVF 100ML', 'MULTIPLE ELECTROLYTES 500ML IVF',
       'SODIUM CHLORIDE 0.9%', 'PANTOPRAZOLE 40MG INJ', 'ONDANSETRON 2MG/ML']


Selected_Drug = st.selectbox("Drug name",Brand)

Selected_period = st.number_input("Enter period(in months) to forecast", min_value=1)
t = pd.date_range(start='2023-01-01' ,periods=Selected_period, freq='MS')
#t=t.strftime("%Y-%m-%d")
_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color:#e7e7e7;
    color: black;
}
div.stButton > button:hover {   
    background-color: #53CFBE;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)

if col.button('Forecast'):
    if Selected_Drug=="NORADRENALINE 2ML INJ":
        pred = model_NORADRENALINE.predict(start=t[0],end = t[-1], typ='levels').rename('NORADRENALINE 2ML INJ')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="SEVOFLURANE 99.97%":
        pred = model_SEVOFLURANE.predict(start=t[0],end = t[-1], typ='levels').rename('SEVOFLURANE 99.97%')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="LEVOSALBUTAMOL/LEVALBUTEROL 0.63MG RESPULES":
        pred = model_LEVOSALBUTAMOL.predict(start=t[0],end = t[-1], typ='levels').rename('LEVOSALBUTAMOL/LEVALBUTEROL 0.63MG RESPULES')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="WATER FOR INJECTION 10ML SOLUTION":
        pred = model_WATER_FOR_INJECTION.predict(start=t[0],end = t[-1], typ='levels').rename('WATER FOR INJECTION 10ML SOLUTION')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="PARACETAMOL 1GM IV INJ":
        pred = model_PARACETAMOL.predict(start=t[0],end = t[-1], typ='levels').rename('PARACETAMOL 1GM IV INJ')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="SODIUM CHLORIDE IVF 100ML":
        pred = model_SODIUM_CHLORIDE_IVF.predict(start=t[0],end = t[-1], typ='levels').rename('SODIUM CHLORIDE IVF 100ML')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="MULTIPLE ELECTROLYTES 500ML IVF":
        pred = model_MULTIPLE_ELECTROLYTES.predict(start=t[0],end = t[-1], typ='levels').rename('MULTIPLE ELECTROLYTES 500ML IVF')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="SODIUM CHLORIDE 0.9%":
        pred = model_SODIUM_CHLORIDE.predict(start=t[0],end = t[-1], typ='levels').rename('SODIUM CHLORIDE 0.9%')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    elif Selected_Drug=="PANTOPRAZOLE 40MG INJ":
        pred = model_PANTOPRAZOLE.predict(start=t[0],end = t[-1], typ='levels').rename('PANTOPRAZOLE 40MG INJ')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    else:
        pred = model_ONDANSETRON.predict(start=t[0],end = t[-1], typ='levels').rename('ONDANSETRON 2MG/ML')
        pred = pd.DataFrame(pred)
        pred = pred.rename_axis('Date').reset_index()
        st.write(pred)
    

st.markdown("""
<style>
div[class="stNumberInput"] > div {
    background-color: #A4DCC5;
    width: 600px;
}
</style>""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-baseweb="input"] > div {
    background-color: #A4DCC5;
}
</style>""", unsafe_allow_html=True)

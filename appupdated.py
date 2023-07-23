# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st
from pickle import dump
from pickle import load
import pickle
import streamlit.components.v1 as com
import base64

# giving a title
st.title('Retinopathy Diabetic Predictor')
st.sidebar.header('User Input Parameters')
       

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())þy
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-repeat: no-repeat;
        background-size: 1925px 1100px
        
    }}
    </style>
    """,
    unsafe_allow_html=True)
    
add_bg_from_local('3.jpg') 



data = pd.read_csv('pronostico_dataset.csv')
array = data.values
X = array[:,0:-1]

loaded_model = load(open('SVC.sav','rb'))


# creating function for prediction
def predict(input_data):
    
    # changing the input data to numpy array 
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 1):
        return st.error("Retinopathy Found")
    else:
        return st.success('Retinopathy Not Found')



def main():
        # getting the input data from the user
        number_1 = st.sidebar.number_input('Insert the AGE of the Patient')
        number_2 = st.sidebar.number_input('Insert the Systolic_Bp of the Patient')
        number_3 = st.sidebar.number_input('Insert the Diastolic_Bp of the Patient')
        number_4 = st.sidebar.number_input('Insert the Cholesterol of the Patient')
        
        
        # code for Prediction
        diagnosis = ''
        
        # creating a button for Prediction
        if st.sidebar.button('Diabetes Test Result'):
            diagnosis = predict([number_1,number_2,number_3,number_4])
            
       
        st.subheader("Mentor :- ")
        st.text("Rajashekhar")
        st.text("Pallavi")
        
        
        
        st.subheader("Made By :- ")
        st.text("Ashutosh Jha")
        st.text("Sameer Herkal")
        st.text("Suresh Solanki")
        st.text("Aditya Mhadye")
        st.text("Krunal Bidkar")

            
    
if __name__ == '__main__':
    main()



# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
# from pickle import dump
from pickle import load

st.title('Model Deployment: Logistic Regression')

st.sidebar.header('User Input Parameters')


def user_input_features():
    age = st.sidebar.number_input("Insert the Age")
    systolic_bp = st.sidebar.number_input("Insert the systolic_bp")
    diastolic_bp = st.sidebar.number_input("Insert the diastolic_bp")
    cholesterol = st.sidebar.number_input("Insert the cholesterol")

    data = {'age': age,
            'systolic_bp': systolic_bp,
            'diastolic_bp': diastolic_bp,
            'cholesterol': cholesterol,
            }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# load the model from disk
loaded_model = load(open('SVC.sav', 'rb'))

prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df)

st.subheader('Predicted Result')
st.write('A patient will suffer from diabetic retinopathy' if prediction_proba[0][1] > prediction_proba[0][
    0] else 'No, A patient will not suffer from diabetic retinopathy')

st.subheader('Prediction Probability')
st.write(prediction_proba)



import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image



def app():
    st.title("Churn Prediction")
    st.write('''
    The customer churn, also known as customer attrition, refers to the phenomenon whereby a customer leaves a company. 
    Some studies confirmed that acquiring new customers can cost five times more than satisfying and retaining existing customers. 
    
    In this project, the goal is to predict the probability of a customer is likely to churn using machine learning techniques.
    ''')
    
    
    st.image(Image.open("churn.png"))


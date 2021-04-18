import streamlit as st
import pickle
import pandas as pd
import numpy as np 
from PIL import Image


pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

st.title("Churn Prediction")
st.write('''
The customer churn, also known as customer attrition, refers to the phenomenon whereby a customer leaves a company. 
Some studies confirmed that acquiring new customers can cost five times more than satisfying and retaining existing customers. 
    
In this project, the goal is to predict the probability of a customer is likely to churn using machine learning techniques.
''')
    
st.image(Image.open("churn.png"))



def predict_churn(Geography, Gender, Age, Balance, 
                  NumOfProducts, HasCrCard, EstimatedSalary):
    input = np.array([[Age, Balance, NumOfProducts, HasCrCard, EstimatedSalary]]).astype(np.float64)
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
        
    if Geography == "France":
        Geography = 0
    elif Geography == "Germany":
        Geography = 1
    else:
        Geography = 2
        
    prediction = model.predict([[Geography, Gender, Age, Balance, NumOfProducts, HasCrCard, EstimatedSalary]])
    
    if prediction == 0:
        pred = 'likely to leave'
    else:
        pred = 'likely to stay'
    return pred
    
def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Churn Prediction App </h2>
    </div>"""
    st.markdown(html_temp, unsafe_allow_html = True)
    Geography = st.selectbox("Geography",["France", "Germany", "Spain"])
    Gender = st.selectbox("Gender",["Male", "Female"])
    Age = st.slider("Age",18,92)
    Balance = st.number_input("Balance")
    NumOfProducts = st.selectbox("Number Of Products Possessed",["1", "2", "3", "4"])
    HasCrCard = st.selectbox("Has Credit Card",["0", "1"])
    EstimatedSalary = st.number_input("Estimated Salary")
    result =""
    if st.button("Predict"):
        result = predict_churn(Geography, Gender, Age, 
                               Balance, NumOfProducts, HasCrCard, EstimatedSalary)
        st.success('The customer is {}'.format(result))
        print(result)

if __name__ == '__main__':
    main()
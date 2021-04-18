import streamlit as st
import pickle
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

def app():
    st.title("Churn Prediction ML APP")
    st.write('''
    Enter the features below, then this app will help you to identify if the person is likely to stay or leave. 
    ''')
    return "welcome"

# csv_file = '../Capstone-master/Churn_Modelling.csv'    
data = pd.read_csv("Churn_Modelling.csv")
data = pd.DataFrame(data)

churn_categorical =['Geography', 'Gender', 'NumOfProducts', 'HasCrCard']
churn = pd.get_dummies(data, columns= churn_categorical)

X = churn.drop(["RowNumber","CustomerId", "Surname", "Exited", "IsActiveMember","Tenure", "CreditScore"], axis = 1)
y = churn['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(StandardScaler(), RandomForestClassifier(max_depth=4, random_state =10))
model.fit(X_train, y_train)


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
    
    
    
    
    # def predict_churn(Geography, Gender, Age, Balance, 
    #               NumOfProducts, HasCrCard, EstimatedSalary):
    #     input = np.array([[Age, Balance, NumOfProducts, HasCrCard, EstimatedSalary]]).astype(np.float64)
    #     if Gender == "Male":
    #         Gender = 0
    #     else:
    #         Gender = 1
        
    #     if Geography == "France":
    #         Geography = 0
    #     elif Geography == "Germany":
    #         Geography = 1
    #     else:
    #         Geography = 2
        
        # prediction = model.predict([[Geography, Gender, Age, Balance, NumOfProducts, HasCrCard, EstimatedSalary]])
    
        # if prediction == 0:
        #     pred = 'likely to leave'
        # else:
        #     pred = 'likely to stay'
        # return pred
    
    # def main():
    #     html_temp = """
    #     <div style="background:#025246 ;padding:10px">
    #     <h2 style="color:white;text-align:center;"> Churn Prediction App </h2>
    #     </div>"""
    #     st.markdown(html_temp, unsafe_allow_html = True)
    #     Geography = st.selectbox("Geography",["France", "Germany", "Spain"])
    #     Gender = st.selectbox("Gender",["Male", "Female"])
    #     Age = st.slider("Age",18,92)
    #     Balance = st.number_input("Balance")
    #     NumOfProducts = st.selectbox("Number Of Products Possessed",["1", "2", "3", "4"])
    #     HasCrCard = st.selectbox("Has Credit Card",["0", "1"])
    #     EstimatedSalary = st.number_input("Estimated Salary")
    #     result =""
    #     if st.button("Predict"):
    #         result = predict_churn(Geography, Gender, Age, 
    #                                Balance, NumOfProducts, HasCrCard, EstimatedSalary)
    #         st.success('The customer is {}'.format(result))
    #         print(result)

    # if __name__ == '__main__':
    #     main()
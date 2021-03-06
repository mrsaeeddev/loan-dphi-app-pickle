import pickle
import streamlit as st
import pandas as pd
import numpy as np


pickle_in = open('classifier.pkl', 'rb') 
model = pickle.load(pickle_in)

def predict(model, input_df):
    prediction_array = np.array([input_df['Gender'][0], input_df['Married'][0], input_df['Dependents'][0],input_df[ 'Education'][0], input_df['Self_Employed'][0], input_df['ApplicantIncome'][0],input_df['CoapplicantIncome'][0], input_df['LoanAmount'][0], input_df['Loan_Amount_Term'][0],input_df['Credit_History'][0], input_df['Property_Area'][0]])              
    final_array = [prediction_array[0],prediction_array[1],prediction_array[2],prediction_array[3],prediction_array[4],prediction_array[5],prediction_array[6],prediction_array[7],prediction_array[8],prediction_array[9],prediction_array[10]]
    predictions = model.predict([final_array])
    return predictions

def run():

    from PIL import Image
    st.set_page_config(page_title='Loan Eligibility App')
    st.sidebar.header('Loan Eligibility App')
    image_loan = Image.open('loan.jpg')

    st.sidebar.info('This app is created to predict whether an applicant is eligible for a loan or not.')
    st.sidebar.success('http://saeed.js.org')
    
    st.sidebar.image(image_loan,use_column_width=True)

    st.title("Please fill this form")

    gender = st.selectbox('Gender', ['Male', 'Female'])
    if st.checkbox('Married'):
        married = 'yes'
    else:
        married = 'no'
    
    dependents = st.selectbox('Dependents', [0,1,2,'3+'])
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_emp = st.selectbox('Self Employed', ['Yes', 'No'])

    applicant_income = st.number_input('Applicant Income', min_value=500, max_value=10000, value=500)
    coapplicant_income = st.number_input('Coapplicant Income', min_value=500, max_value=10000, value=500)
    loan_amount = st.number_input('Loan Amount', min_value=100, max_value=10000, value=100)

    loan_amount_term = st.selectbox('Loan Amount Term', [110,200,360])

    credit_history = st.selectbox('Credit History', [0,1])
    property_area = st.selectbox('Property Area', ['Semiurban', 'Rural', 'Urban'])

    output=""

    input_dict = {
                    'Gender' : gender,
                    'Married' : married,
                    'Dependents' : dependents, 
                    'Education' : education,
                    'Self_Employed' : self_emp,
                    'ApplicantIncome': applicant_income,
                    'CoapplicantIncome': coapplicant_income,
                    'LoanAmount': loan_amount,
                    'Loan_Amount_Term': loan_amount_term,
                    'Credit_History': credit_history,
                    'Property_Area': property_area
                    }
    input_df = pd.DataFrame([input_dict])

    input_df = input_df.apply(lambda x: x.astype('category').cat.codes)
    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        if output == 1:
            
            st.success('The applicant is eligible for loan')
        else:
            st.error('The applicant is not eligible for loan')

if __name__ == '__main__':
    run()
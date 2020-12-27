from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('deployment_28042020')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image_loan = Image.open('loan.jpg')

    # add_selectbox = st.sidebar.selectbox(
    # "How would you like to predict?",
    # ("Online", "Batch"))

    st.sidebar.info('This app is created to predict whether an applicant is eligible for a loan or not.')
    st.sidebar.success('http://saeed.js.org')
    
    st.sidebar.image(image_loan,use_column_width=True)

    st.title("Loan Eligibility App")

    # if add_selectbox == 'Online':
        # load_id = 'LP'
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

        

    # if add_selectbox == 'Batch':

    #     file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

    #     if file_upload is not None:
    #         data = pd.read_csv(file_upload)
    #         predictions = predict_model(estimator=model,data=data)
    #         st.write(predictions)

if __name__ == '__main__':
    run()
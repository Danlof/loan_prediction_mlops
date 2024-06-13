# importing dependencies

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np
import pandas as pd

app = FastAPI()
model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

# performing parsing 

class LoanPred(BaseModel):
    Gender: float
    Married: float
    Dependents: float
    Education: float
    Self_Employed: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: float
    TotalIncome: float

@app.get("/")
def index():
    return {'Message':'Welcome to Loan Application App'}

# defining the function which will make the prediction using the data which the user inputs 
@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
    data = loan_details.model_dump()
    gender = data['Gender']
    married = data['Married']
    dependents = data['Dependents']
    education = data['Education']
    self_employed = data['Self_Employed']
    loan_amt = data['LoanAmount']
    loan_term = data['Loan_Amount_Term']
    credit_hist = data['Credit_History']
    property_area = data['Property_Area']
    income = data['TotalIncome']

    # making predictions 
    prediction = model.predict([[gender, married, dependents, education, self_employed, loan_amt, loan_term, credit_hist, property_area,income]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return {'Status of the loan applied is': pred}

if __name__ =='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)



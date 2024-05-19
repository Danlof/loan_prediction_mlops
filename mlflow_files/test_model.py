# Puprpose of this file is to make predictions using one of the best models 

import mlflow
logged_model = 'runs:/6282c408e01f4297b656b2c09de2265c/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
columns  = [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
            "TotalIncome"
        ]

data = [
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    4.98745,
    360.0,
    1.0,
    2.0,
    8.698
        ]
data_df = pd.DataFrame([data],columns=columns)

# make predictions 
predictions = loaded_model.predict(data_df)
print(predictions)

if  predictions[0] == 1:
    print(" Loan was succesfully approved")
else:
    print("Unsuccessful Loan application")
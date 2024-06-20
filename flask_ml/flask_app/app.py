from flask import Flask,render_template,request
import numpy as np
import joblib
import pandas as pd 

app = Flask(__name__)

# load training model
model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

# app
@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/predict",methods=['POST'])
def predict():
    if request.method =='POST':
        request_data = dict(request.form)
        del request_data['First_Name']
        del request_data['Last_Name']
        request_data = {k:int(v) for k,v in request_data.items()}
        data = pd.DataFrame([request_data])
        data['TotalIncome'] = data['applicant_income'] + data['co_applicant_income']
        data['TotalIncome'] = np.log(data['TotalIncome']).copy()
        # Rearrange and select only the columns which are required for prediction
        data = data[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area','TotalIncome']]
        prediction = model.predict(data)
        prediction_value = prediction[0]

        if int(prediction_value) == 1:
            result = "Congratulations! your loan request is approved"
        if int(prediction_value) == 0:
            result = "Sorry! your loan request is rejected"
        
        return render_template('homepage.html',prediction = result)
    
    @app.errorhandler(500)
    def internal_error(error):
        return "500: Something went wrong"
    
    @app.errorhandler(404)
    def not_found(error):
        return "404:page not found",404
    
    if __name__=="__main__":
        app.run(host='0.0.0.0',port=80)

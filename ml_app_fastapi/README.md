- Runing the `demo.py` use `uvicorn demo:app --reload` # the demo is the name of the file.py and the `app` is the fastapi object created.
- if you want to get automatic documentation use the `https:\\<your running address>/docs` or `https:\\<your running address>/redoc`

- We will use the following methods :
    -  `POST` to create data
    - `GET` to read the data
    - `PUT` to update data
    - `DELETE` to delete data 

- to perform different operations we use ;
    - `app.post()`
    - `app.put()`
    - `app.delete()`

### Loan prediction 
- I will create an app using fastapi to make approvals or jects on applications of loans. 
This can be found on `loan_fastapi_app.py`
- The `BaseModel` helps to maintain consistency on the data types even when a client enters the incorrect data types it corrects them for consistent modelling.
- Then you can run the app via the terminal using `python3 loan_fastapi_app.py`

- json data for prediction:

`{
  "Gender": 1,
  "Married": 0,
  "Dependents": 0,
  "Education": 2,
  "Self_Employed": 0,
  "LoanAmount": 5.0,
  "Loan_Amount_Term": 250.0,
  "Credit_History": 2.0,
  "Property_Area": 1.0,
  "TotalIncome": 9.2
}`

- You can also use curl as follows:
`curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Gender": 0,
  "Married": 0,
  "Dependents": 0,
  "Education": 0,
  "Self_Employed": 0,
  "LoanAmount": 0,
  "Loan_Amount_Term": 0,
  "Credit_History": 0,
  "Property_Area": 0,
  "TotalIncome": 0
}`
`
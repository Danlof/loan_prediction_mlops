# Build the package 
`pip install -r requirements.txt`

2 . Create a pickle file after training 
`python prediction_model/training_pipeline.py`

3. Create source distribution and the wheel
`python setup.py sdist bdist_wheel`

4. To install ml flow
`python3 -m venv flowenv`
`pip install mlflow`

5. Activate the Mlflow user interface 
`mlflow ui`

# Notes of Mlflow tracking 
`mlflow.set_tracking_uri()` - connects to tracking uri(uniform resource identifier).You can also set the MLFLOW_TRACKING_URI environment variable to have MLFOW  find a URI from there .

`mlflow.get_tracking_uri()` - returns the current tracking URI

`mlflow.create_experiment`- creates a new experiment and returns its id. Runs can be launched under the experiment by passing the experiment ID to mlflow.start_run()

`mlflow.set_experiment` - sets an experiment as active.If the experiment does not exist, creates a new experiment. If you do not specify an experiment in mlflow.start_run(), new runs are launched under this experiment.

`mlflow.start_run`- returns the currently active run, or starts a new  run and returns a mlflow.ActiveRun object used as a content manager for the current run.You do not need to call start_run explicitly: calling one of the logging functions with no active run automatically starts a new one.

`mlflow.end_run()` - ends the currently active run, if any, taking an optional run status

`mlflow.log_param()` - logs in a single key-value in the currently active run.The key and value are both strings.Use mlflow.log_params()  to log multiple params at once.

`mlflow.log_metric()` logs in a single key-value.The value must be a number. Mlflow remembers the history values of each metric.  Use mlflow.log_metrics() to log multiple metrics at once.

`mlflow.set_tag()`- sets a single key-value tag in the currently active run.the key-value are both strings.Use mlflow.set_tags() to set multiple tags at once.

`mlflow.log_artifacts()` - logs all files in a given directory as artifacts ,taking  an optional artifact_path.

### If port is arealdy in use 
- Get a list of the services & PID running using - `sudo lsof -i tcp:5000`
- Kill them using `kill -15 <PID> `


# Mlflow Projects 
- Create a run using mlflow project file `mlflow run . --experiment-name <name_of_experiment>`. Run from the folder where MLProject file is present 

- Run from git repository `mlflow run https://github.com/<reponame> --experiment-name <name_of_experiment>`


# mlflow models
- serve model with local host server `mlflow models serve -m ///media/danlof/dan%20files/data_science_codes/udemy_course/mlflow_files/mlruns/976328977400062323/6282c408e01f4297b656b2c09de2265c/artifacts/RandomForestClassifier --port 9000`

- sign up for postman and post this :`http://127.0.0.1:9000/invocations`

- the run this as a json file on the raw column:

`
{
    "dataframe_split": {
        "columns": [
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
        ],
        "data": [
            [
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
        ]
    }
}
`

- you can also run the following on your local terminal :
`
curl --location 'http://127.0.0.1:9000/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "dataframe_split": {
        "columns": [
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
        ],
        "data": [
            [
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
        ]
    }
}'
`
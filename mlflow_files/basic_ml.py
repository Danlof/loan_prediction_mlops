# This file is for educational purpose and should be ignored 

import os
import mlflow
import argparse
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np 
import pandas as pd
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

 
# load the dataframe for wines 
def load_data():
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    try:
        df = pd.read_csv(URL,sep=";")
        return df
    except Exception as e:
        raise e

# evaluation function metrics    
def eval_function(actual,pred):
    rmse = mean_squared_error(actual,pred,squared=False)
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse,mae,r2
    
def main(alpha,l1_ratio):
    """loads x and y, splits the data and logs metrics and the model to mlflow"""
    df = load_data()
    TARGET = "quality"
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=43)

    mlflow.set_experiment("ML_Model-1")
    with mlflow.start_run():
        # log the user inputs 
        mlflow.log_param("alpha",alpha) 
        mlflow.log_param("l1_ratio",l1_ratio)

        model = ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=43)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        # evaluation
        rmse,mae,r2 = eval_function(y_test,y_pred)
        # log the metrics above 
        mlflow.log_metric("rmse",rmse)
        mlflow.log_metric("mae",mae)
        mlflow.log_metric("r2",r2)
        # finally we can log in the model
        mlflow.sklearn.log_model(model,"trained model") # model name and folder of the model

# start by reading the input from the user
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha","-a", type=float, default=0.2)
    args.add_argument("--l1_ratio","-l1", type=float, default=0.3)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.alpha, parsed_args.l1_ratio)
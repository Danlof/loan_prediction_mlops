import argparse
import os 
import warnings

import numpy as np
import pandas as pd 

from sklearn.linear_model import  ElasticNet
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split 

import mlflow
import mlflow.sklearn

def eval_metrics(actual,pred):
    rmse = np.sqrt(mean_absolute_error(actual,pred))
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse,mae,r2

if __name__=="__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(23)
    
    # gets the input from the user 
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha",type=float, required=True)
    parser.add_argument("--l1_ratio",type=float, required=True)
    args = parser.parse_args()

    wine_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"winequality-white.csv")
    data = pd.read_csv(wine_path,delimiter=';')
    # split the data into training and test sets.
    train,test = train_test_split(data)

    # the predicted value is qualinty which is between [3,9]
    x_train = train.drop(['quality'],axis=1)
    x_test = test.drop(['quality'],axis=1)
    y_train= train[['quality']]
    y_test = test[['quality']]

    alpha = float(args.alpha)
    l1_ratio = float(args.l1_ratio)

    with mlflow.start_run():
        lr = ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=23)
        lr.fit(x_train,y_train)

        predicted_qualities = lr.predict(x_test)

        (rmse,mae,r2) = eval_metrics(y_test,predicted_qualities)

        print(f"Elastic Model (alpha={alpha:f},l1_ratio={l1_ratio:f}):")
        print(f"RMSE: {rmse}")
        print(f"MAE: {mae}")
        print(f"R2: {r2}")

        mlflow.log_param("alpha",alpha)
        mlflow.log_param("l1_ratio",l1_ratio)
        mlflow.log_metric('rmse',rmse)
        mlflow.log_metric('mae',mae)
        mlflow.log_metric('r2',r2)

        mlflow.sklearn.log_model(lr,"model")





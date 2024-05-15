import os
import mlflow
import argparse
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np 
import pandas as pd

# start by reading the input from the user 


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha","-a", type=float, default=0.2)
    args.add_argument("--l1_ratio","-l1", type=int, default=0.3)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.alpha, parsed_args.l1_ratio)
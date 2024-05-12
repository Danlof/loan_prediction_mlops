import mlflow
import argparse
import os
import time 


# get the inputs from the user 
# you can start making various transformations 
def eval(p1,p2):
    output_metric = p1**2 + p2**2
    return output_metric

def  main(input1,input2):
    with mlflow.start_run(run_name='Example Demo'):
        mlflow.log_param('param1',input1)
        mlflow.log_param('param2',input2)
        metric = eval(p1 = input1,p2=input2)
        mlflow.log_metric('Eval_Metric',metric)
        os.makedirs('dummy',exist_ok= True)
        with open('dummy/example.txt','wt') as f:
            f.write(f"Artifacts created at {time.asctime()}") 
        mlflow.artifacts("dummy")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--param1','-p1',type = int,default = 5)
    args.add_argument('--param2','-p2',type = int,default = 10)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.param1,parsed_args.param2)

FROM  python:3.10.12

RUN pip install mlflow numpy scipy pandas scikit-learn cloudpickle

COPY train.py .

COPY winequality-white.csv .
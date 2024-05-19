# MLOPS
- A loan model that is predicting if a given person will given  a loan based on a few parameters.

### From the `mlflow_files` packages

- I am using 3 models to do the prediction : `random forests classifier, logistic regression classifier and decision tree classifier`
- `Mlflow` is used for managing the experiments
- Metrics such are `f1 score, accuracy and AUC` are compared in all 3 models and the random classifier is picked based on the above by out performing the other 2 models.
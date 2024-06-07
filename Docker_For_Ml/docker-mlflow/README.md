### Build an image 
`docker build -t mlflow-docker-elasticnet .`

- Incase you get an error requiring you to add the parameters `alpha` and `l1_ratio` use one of the these methods: 
    - have the default values in the MLProject 
    - give the value parameters via the command line i.e `mlflow run . -P alpha=0.1 -P l1_ratio=0.01`
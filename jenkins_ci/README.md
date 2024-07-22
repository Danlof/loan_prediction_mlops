### Some commands used to run docker, locally.
```
docker build -t danlof/cicd:latest . #-->  This builds the docker image
docker push danlof/cicd:latest # pushes the images to the docker hub

docker run -d -it --name modelv1 -p 8005:8005 danlof/cicd:latest bash # creates a docker image on the port 8005

docker exec modelv1 python prediction_model/training_pipeline.py # excecutes the training pipeline on that containeer 

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear # ensure good quality of code 

docker cp modelv1:/code/src/TestResults.xml . 

docker exec -d -w /code modelv1 python main.py # execute the 
```
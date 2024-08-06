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

## using Jenkins 
- Got t0 the official documentations of jenkins on how to install it together with java.
-

### Enabling jenkins 
`sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
`
### Installing docker
- Next install docker (instructions on the official website of linux docker installation)
`
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
`

- to run the latest version use :
`
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
`
- verify docker is intalled :
`sudo docker run hello-world`


- These 2 commands enable permissions on jenkins
`sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER
`
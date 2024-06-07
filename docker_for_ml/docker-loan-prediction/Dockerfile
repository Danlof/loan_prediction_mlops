# base image 
FROM python:3.10-slim

# upgrade pip 
RUN pip install --upgrade pip

# copying all files to a source directory
COPY . /src 

# setting the working directory previously addded

WORKDIR /src

# give permission to python files 

RUN chmod +x docker_train.py

# install dependencies 

RUN pip install -r requirements.txt

# run docker_file.py
ENTRYPOINT [ "python" ]

CMD [ "docker_train.py" ]

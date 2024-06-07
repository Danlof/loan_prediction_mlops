FROM python:3.10.12

# setting a directory for the app
WORKDIR /usr/src/app

# copying all the files to the containter 

COPY . .

# installing dependencies 

RUN pip install --no-cache-dir -r requirements.txt

# tell the container the number of port it should expose 

EXPOSE 5000

# run the command 

CMD [ "python","./app.py" ]


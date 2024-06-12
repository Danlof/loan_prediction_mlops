- Runing the `demo.py` use `uvicorn demo:app --reload` # the demo is the name of the file.py and the `app` is the fastapi object created.
- if you want to get automatic documentation use the `https:\\<your running address>/docs` or `https:\\<your running address>/redoc`

- We will use the following methods :
    -  `POST` to create data
    - `GET` to read the data
    - `PUT` to update data
    - `DELETE` to delete data 

- to perform different operations we use ;
    - `app.post()`
    - `app.put()`
    - `app.delete()`

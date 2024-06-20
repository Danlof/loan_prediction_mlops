## Create a flask app
- create a  virtual envirnment `python -m venv <environmentname>`
- activate the environment `source <enviromentname>/bin/activate`
- install requirements.txt `pip install requirements.txt`
- Run the `main.py` file `flask --app main run` 
- if you add 
```
if __name__=="__main__":
    app.run()
```
you can simply call it using `python main.py`
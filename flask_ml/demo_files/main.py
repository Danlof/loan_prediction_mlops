from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Flask Application</h1>"

@app.route("/welcome")
def welcome():
    return "<h2>Welcome navigation</h2>"

@app.route("/welcome/<user>")
def welcome_user(user):
    return f"<h2>Welcome {user} to Flask 101</h2>"

if __name__=="__main__":
    app.run()

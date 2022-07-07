from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    return "<h1>Hello, world!</h1>"


    # x = index() # function call

@app.get("/about")
def get_about():
    me = {
        "first_name": "Arthur",
        "last_name": "Murphy",
        "hobbies": "Youth baseball",
        "active": True
    }
    return me

from flask import Flask             # From the flask module import the Flask class

                                    # Create an instance of the Flask class into app.
app = Flask(__name__)
                                    # app is now an "object"
                                    
@app.get("/")                       # Flask decorator that allows us to map a route to a view function
def index():                        # Our view function
    return "<h1>Hello, world!</h1>"   # Return statement.

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

#!/usr/bin/python3
"""Flask framewoek
"""
from flask import Flaskq

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """returm hello hbnb
    """
    return "Hello HBNB"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """return text given"""
    return "C {}".format(text.replace("_"," "))


@app.route('/python/', defaults ={'text' : 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """return Python follwed by given text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ =="__main___":
    app.run()

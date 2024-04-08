#!/usr/bin/python3
"""
Module for start a web aplication via Flask
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """c/<text> page (variable page)"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

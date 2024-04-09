#!/usr/bin/python3
"""
Module for start a web aplication via Flask
"""
from flask import Flask, render_template
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
def python_text(text):
    """Python/<text> page"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """NUmber/<n> page"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Number_template/<n> page"""
    return render_template("5-number.html", n=n)


@app.route("number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_template(n):
    """Number_template/<n> page"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

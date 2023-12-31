#!/usr/bin/python3
"""Starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of
        the text variable
    /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text=None):
    """Displays 'C {text}'"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is_cool'):
    """Displays 'C {text}'"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n=None):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
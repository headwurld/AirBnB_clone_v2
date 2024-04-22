#!/usr/bin/python3
"""Starts flask web application, on host '0.0.0.0' port 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """A web page displaying
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb web page, displaying HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display C followed by the text passed as first argument
    """
    contain = text.replace('_',' ')
    return f"C {contain}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

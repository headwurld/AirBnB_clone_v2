#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """display ththe value of the variable text"""
    return f'c {escape(text)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text="is cool"):
    """display python and tehe variabke text"""
    return f'python {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
This script defines a Flask application with four routes:
- '/'
- '/hbnb'
- '/c/<text>'
- '/python/' (default value of 'text' is 'is cool')
- '/python/<text>'

The routes return strings based on the input text.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python ' + text.replace('_', ' ')

# Test case for "/python/<text>" route
def test_python_route():
    import requests
    response = requests.get('http://localhost:5000/python/test')
    assert response.text == 'Python test'

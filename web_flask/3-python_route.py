#!/usr/bin/python3
""" script that starts a Flask web application  """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    text = text.replace('_', ' ')
    return 'python %s' % escape(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

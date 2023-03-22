#!/usr/bin/python3
# starts flask with c thing
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    return 'C ' + text.replace("_", ' ')


@app.route('/python/')
@app.route('/python/<text>')
def ptext(text='is cool'):
    return 'Python {}'.format(text.replace("_", ' '))


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)

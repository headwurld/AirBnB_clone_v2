#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return “Hello HBNB!”


@app.route("/about", strict_slashes=False)
def about():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

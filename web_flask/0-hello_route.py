#!/usr/bin/python3
"""Script starts flask application, listening 0.0.0.0:5000
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
"""display Hello HBNB! on this route"""
def home{}:
    """my web server home page"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    """run the app on host 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)

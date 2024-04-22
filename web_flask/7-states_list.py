#!/usr/bin/python3
"""Script starts a Flask web application
"""
from flask import Flask
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page """
    states = storage.all("state").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

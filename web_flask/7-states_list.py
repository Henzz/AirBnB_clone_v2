#!/usr/bin/python3
"""
A script that starts a Flask web application with 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list(n):
    """
    '/number_template/<n>' route page
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    tear down
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

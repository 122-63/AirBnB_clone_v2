#!/usr/bin/python3
"""List of states"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes=False

states = storage.all(State).values()


@app.route('/states_list')
def states():
    """states"""
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """close session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

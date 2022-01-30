#!/usr/bin/python3
""" starts a flask web application
    display “C ” followed by the value of the text"""


from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb1():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_hbnb2(text):
    """return “C ” followed by the value of the text"""
    return 'C %s' % escape(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

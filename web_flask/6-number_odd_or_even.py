#!/usr/bin/python3
""" starts a flask web application
    display “C ” followed by the value of the text"""


from flask import Flask, escape, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_hbnb3(text):
    """return "python" default=is cool or followed dy the
       value of the text"""
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>')
def show_post(n):
    """show the post with the given id, the id is an integer"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_hbnb5(n):
    """ template number"""
    return render_template('5-number.html', n=n)


@app.route('number_odd_or_even/<int:n>', strict_slashes=False)
def hello_hbnb6(n):
    """if "n" is odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

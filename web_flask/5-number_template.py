#!/usr/bin/python3
"""
A script that starts a Flask web application with 0.0.0.0, port 5000
"""
from flask import render_template, Flask
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """
    '/' route page
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    """
    '/hbnb' route page
    """
    return "HBNB"


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def c(text):
    """
    '/c/<text>' route page
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def pythonParam(text='is cool'):
    """
    '/python/<text>' route page
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    '/number/<n>' route page
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number(n):
    """
    '/number/<n>' route page
    """
    return render_template('./templates/5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

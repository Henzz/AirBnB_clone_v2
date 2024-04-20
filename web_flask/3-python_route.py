#!/usr/bin/python3
"""
A script that starts a Flask web application with 0.0.0.0, port 5000
"""
from flask import Flask
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
def pythonParam(text='is cool'):
    """
    '/python/<text>' route page
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

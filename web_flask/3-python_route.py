#!/usr/bin/python3
"""
A script that starts a Flask web application with 0.0.0.0, port 5000
"""
from flask import abort, Flask
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
def cParam(text=None):
    """
    '/c/<text>' route page
    """
    if text:
        return "C"+' '+text.replace('_', ' ')
    else:
        abort(404)


@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def pythonParam(text="is cool"):
    """
    '/python/<text>' route page
    """
    if text:
        return "Python"+' '+text.replace('_', ' ')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

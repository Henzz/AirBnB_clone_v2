#!/usr/bin/python3
"""
A script that starts a Flask web application with 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", 'GET', '', False)
def hello_work():
    """
    '/' route page
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

#!/usr/bin/python3
"""AirBnB - Web Framework
3 - Python is cool!"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def heybuddy():
    """Returns 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def textual(text):
    """Displays "C <text>, no underscores, undaspaces"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text="is cool"):
    """Displays "Python <text>, no underscores, undaspaces"""
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

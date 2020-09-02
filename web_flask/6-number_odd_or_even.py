#!/usr/bin/python3
"""AirBnB - Web Framework
6 - Odd or even?"""
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def numbas(n):
    """Displays "<n> is a number" only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbas_temp(n):
    """Displays a HTML page with "Number: <n>", H1 tag, inside BODY"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbas_oddeven_temp(n):
    """Displays a HTML page with "Number: <n> is even|odd", H1, in BODY"""
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""AirBnB - Web Framework
10 - States and State"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
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


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def listates():
    """Displays an HTML page with a list of all State objects, sorted"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def listates_withdacities():
    """Displays an HTML page with a list of all state objects, sorted by name
    with list of city objects linked tos tate, sorted by name below state"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_ur_id(id):
    """Displays an HTML page with State & Cities, sorted, if id is found.
    Otherwise, displays "Not found!" """
    states = storage.all(State).values()
    ids = []
    thestate = ""
    for state in states:
        if state.id == id:
            thestate = state
            ids.append(state.id)
    return render_template('9-states.html', state=thestate, ids=ids)


@app.route('/hbnb_filters', strict_slashes=False)
def habnbfil():
    """filters page"""
    sts = storage.all(State).values()
    amen = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=sts, amenities=amen)


@app.teardown_appcontext
def ripnshred(self):
    """Removes current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

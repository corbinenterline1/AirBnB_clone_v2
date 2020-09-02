<center> <h1>AirBnB clone - Web framework</h1> </center>

This project focuses on using the web framework Flask to generate dynamic content using Jinja2 templates.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Hello Flask! | [0-hello_route.py](0-hello_route.py) | Script that starts flask web app listening on `0.0.0.0`, port `5000`. The route `/` displays "Hello HBNB!"
| 0: init file | [__init__.py](__init__.py) | init file for module.
| 1: HBNB | [1-hbnb_route.py](1-hbnb_route.py) | Same as 0, with route `/hbnb` displaying just "HBNB"
| 2: C is fun! | [2-c_route.py](2-c_route.py) | 1 + new route `/c/<text>` that displays "C" followed by value of `text` variable, replacing underscores with spaces.
| 3: Python is cool! | [3-python_route.py](3-python_route.py) | 2 + new route `/python/(<text>)`: displays "Python" followed by value of `text` variable, replaing underscores with spaces.
| 4: Is it a number? | [4-number_route.py](4-number_route.py) | 3 + new route `/number/<n>`: displays "`n` is a number" <b>only</b> if `n` is an integer
| 5: Number template | [5-number_template.py](5-number_template.py) | 4 + new route `/number_template/<n>`: displays a HTML page <b>only</b> if `n` is an integer. `H1` tag:"Number: `n`" inside the tag `BODY`
| 5: Template | [5-number.html](templates/5-number.html) | Template for 5.
| 6: Odd or even? | [6-number_odd_or_even.py](6-number_odd_or_even.py) | 5 + new route `/number_odd_or_even/<n>`: displays a HTML page <b>only</b> if `n` is an integer. `H1` tag: "Number: `n` is `even|odd`" inside the tag `BODY`
| 6: Template | [6-number_odd_or_even.html](/templates/6-number_odd_or_even.html) | Template for 6.
| 7: Improve engines | [file_storage.py](/models/engine/file_storage.py) | File storage engine modified with public method `def close(self):`: calls `reload()` method for deserializing the JSOn file to objects.
| 7: Improve engines | [db_storage.py](/models/engine/db_storage.py) | DB Storage engine modified with public method `def close(self):`: calls `remove()` method on the private session attribute (`self.__session`) or `close()` on the class `Session`.
| 7: Improve engines | [state.py](/models/state.py) | If storage engine isn't `DBStorage`, add public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`.
| 8: List of states | [7-states_list.py](7-states_list.py) | Script that starts a Flask web app listening on `0.0.0.0`, port `5000`. Must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`. After each request you must remove the current SQLAlchemy Session. Add route `/states_list`. 
| 8: List of states | [7-states_list.html](/templates/7-states_list.html) | Template for 8.
| 9: Cities by states | [8-cities_by_states.py](8-cities_by_states.py) | New route `/cities_by_states`. To load all cities of a `State`: if `DBStorage`, use `cities` relationship. Otherwise, use the public getter method `cities`. Bit of formatting on the cities by state route.
| 9: Cities by states | [8-cities_by_states.html](/templates/8-cities_by_states.html) | Template for 9
| 10: States and state | [9-states.py](9-states.py) | New routes `/states` and `/states/<id>`.
| 10: States and state | [9-states.html](/templates/9-states.html) | Template for 10.
| 11: HBNB filters | [10-hbnb_filters.py](10-hbnb_filters.py) | New route `/hbnb_filters`: displays a HTML page like 6-index.html
| 11: HBNB filters | [10-hbnb_filters.html](/templates/10-hbnb_filters.html) | Template for 11.
| 12: HBNB is alive! | [100-hbnb.py](100-hbnb.py) | **ADVANCED** Route for `/hbnb` with some fun!
| 12: HBNB is alive! | [100-hbnb.html](/templates/100-hbnb.html) | **ADVANCED** Template for 12
<br>
<br>
<center> <h2>Lessons Learned</h2> </center>
<ul>
  <li>What is Fabric</li>
  <li>How to deploy code to a server easily</li>
  <li>What is a `tgz` archive</li>
  <li>How to execute Fabric command locally</li>
  <li>How to execute Fabric command remotely</li>
  <li>How to transfer files with Fabric</li>
  <li>How to manage NGINX configuration</li>
  <li>What is the difference between `root` and `alias` in a NGINX configuration</li>

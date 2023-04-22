#!/usr/bin/python3
"""Flask framework"""

from flask import Flask, render_template
from models import storage
from model.state import State

app = Fladk(__name__)

@app.teardowm_appcontext
def teardown_db(exception):
    """teardown db"""
    if storage is not None:
        storage.close()


@app.route("/state_list", strict_slashes=False)
def state_list():
    """list of  state ids"""
    data = storage.all(State)
    return render_template("7-states_list.html", total=data.values())


if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000)

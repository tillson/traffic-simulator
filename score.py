#!/usr/bin/python
# Scoring Engine
#
# Porter-Gaud Honors Computer Science IV 2017-2018
# Tillson Galloway
#

from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder="web_scoring")

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route("/scoreboard")
def scoreboard():
    return render_template('scoreboard.html', title='Home')

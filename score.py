#!/usr/bin/python
# Scoring Engine
#
# Porter-Gaud Honors Computer Science IV 2017-2018
# Tillson Galloway
#

from flask import Flask
from flask import render_template, redirect
from flask import request
import json

app = Flask(__name__, template_folder="web_scoring")

flags = json.load(open('data/flags.json'))
teamData = json.load(open('data/data.json'))

@app.route("/")
def index():
    return render_template('index.html', error=request.args.get('error'),
        points=request.args.get('points'),
        submitted=request.args.get('submitted'))

@app.route("/scoreboard")
def scoreboard():
    return render_template('scoreboard.html', title='Home', teamData=teamData)

@app.route("/submit", methods=["POST"])
def submit():
    submittedFlag = request.form["flag"]
    for flag in flags:
        if submittedFlag == flag["flag"]:
            team = [team for team in teamData if team.get('teamname')==request.form["teamname"]]
            if team == []:
                teamData.append({ "teamname": request.form["teamname"], "flags": [flag["flag"]], "score": flag["points"] })
            else:
                team = team[0]
                if flag["flag"] in team["flags"]:
                    return redirect("/?success&submitted=1", code=302)
                team["flags"].append(flag["flag"])
                team["score"] = (team["score"] + flag["points"])
            writeDataToFile()
            return redirect("/?success&points=" + str(flag["points"]), code=302)
    print request.form["teamname"]
    return redirect("/?success&error=1", code=302)

def writeDataToFile():
    with open('data/data.json', 'w') as outfile:
        json.dump(teamData, outfile)

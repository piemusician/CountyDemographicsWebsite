from flask import Flask, request, Markup, render_template, flash, Markup import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('start.html')

def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    with open('all_states.json') as state_data:
        allstates = json.load(state_data)
    if "state" in request.args:
        state = request.args['state']
        return render_template('start.html')


@app.route("/response")
def render_response():

if __name__=="__main__":
    app.run(debug=False, port=54321)
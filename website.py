from flask import Flask, request, Markup, render_template

import os
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', options=get_state_options())
 
@app.route('/funFact')   
def render_fun_fact():
    state_chosen = request.args['state']
    return render_template('home.html', options=get_state_options(), funFact=fun_fact_by_state(state_chosen))
    
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
    	if not(county["State"] in listOfStates):
    		listOfStates.append(county["State"])
    		
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

def fun_fact_by_state(state):
    first_county = "ZZZZZZZ"
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        county["County"]
        if county["County"] < first_county and county["State"] == state:
            first_county = county["County"]
    return "The first county of this state is " + first_county
    


if __name__=='__main__':
    app.run(debug=True, port=54321)

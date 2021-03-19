from flask import Flask, request, Markup, render_template, flash, Markup import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    with open('all_states.json') as state_data:
        allstates = json.load(state_data)
    if "state" in request.args:
        state = request.args['state']
        return render_template('start.html', options1=get_state_options(counties) , options2=get_county_options(counties,state) , funfact1=fun_fact1(state, counties) ,funfact2=fun_fact2(state, counties), _state=the_state(state,allstates) , State1=avb_state(state) , )
        
    if "county" in request.args:
        county = request.args['county']
        state=""
        return render_template('start.html', options1=get_state_options(counties) , options2=get_county_options(counties,state) , funfact1=fun_fact1(state, counties) ,funfact2=fun_fact2(county, counties), _state="" ,_county=county, State1=avb_state(state) )

    if "state" is not request.args:
        state = ""
        return render_template('start.html', options1=get_state_options(counties) , options2=get_county_options(counties,state))
        
    
    if "county" is not request.args:
        county = ""
        return render_template('start.html', options1=get_state_options(counties) , options2=get_county_options(counties,state))
def get_state_options(counties):
    options1=""
    listOfStates=[]
    for x in counties:
        if x["State"] not in listOfStates:
            listOfStates.append(x["State"])
    for x in listOfStates:
        options1 += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options1
def get_county_options(counties,state):
    options2=""
    listOfCounties=[]
    for x in counties:
        if x["County"] not in listOfCounties and x["State"] == state:
            listOfCounties.append(x["County"])
    for x in listOfCounties:
        options2 += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options2
def fun_fact1(state,counties):
    population=0
    for x in counties:
        if state == x["State"]:
            i = x["Population"]["2014 Population"]
            population = population +i
    return "Population: %i" % population
def fun_fact2(county,counties):
    population=0
    for x in counties:
        if county == x["County"]:
            i = x["Population"]["2014 Population"]
            population = population +i
    return "Population: %i" % population
def the_state(state,allstates):
    if not state=="":
        return "State:" + " " + allstates[state]
def the_county(county):
    return county
def avb_state(state):
    return state
if __name__=="__main__":
    app.run(debug=True, port=54321)

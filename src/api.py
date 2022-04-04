from flask import Flask, Response, request
from flask_cors import CORS
import pandas as pd
import os
import numpy as np
from werkzeug import Response
import pickle
app =Flask(__name__)

CORS(app)
training_data = pd.read_csv(os.path.join("data","auto-mpg.csv"))
filename = 'finalized_model_auto.sav'
loaded_model = pickle.load(open(filename, 'rb'))


@app.route("/", methods=["GET"])
def index():
    return{"hello": "world"}


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return"<p>Hello World!</p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/predict" , methods=["GET"])
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")
    if (zylinder and ps and gewicht and beschleunigung and baujahr):
        input_list= [zylinder, ps, gewicht, beschleunigung, baujahr]
        input_array= np.array(input_list).reshape(1,-1)
        prediciton = loaded_model.predict(input_array)
        return {"result": prediciton[0]}

    return Response("please provide all neccesary parameters to get a prediction", mimetype="application/json")

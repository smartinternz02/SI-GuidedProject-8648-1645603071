import numpy as np
import pandas as pd
import os
import joblib
from flask import Flask, jsonify, request, render_template, url_for, redirect, Markup

app = Flask(__name__)
joblib_file = "model.pkl"
model = joblib.load(joblib_file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET','POST'])
def getform():
    if request.method == "GET":
        return (render_template("form.html"))

    if request.method == 'POST':
        if 'submit-button' in request.form:
            diagnosis = request.form["diagnosis"]
            fev = request.form["fev"]
            age = request.form["age"]
            performance = request.form["performance"]
            tnm = request.form["tnm"]
            hae = request.form['hae']
            pain = request.form["pain"]
            dys = request.form["dys"]
            cough = request.form["cough"]
            weakness = request.form["weakness"]
            dm = request.form["dm"]
            mi = request.form["mi"]
            pad = request.form["pad"]
            smoking = request.form["smoking"]
            asthma = request.form["asthma"]
            total = [[diagnosis,fev,age,performance,tnm,hae,pain,dys,cough,weakness,dm,mi,pad,smoking,asthma]]
            prediction = model.predict(total)[0]
 

            if int(prediction) == 1:
                prediction = "Patient is at High Risk"
               
                
            else:
                prediction = "Patient is Not at Risk"
                
            
            return render_template("result.html", prediction = prediction)
    
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=False)


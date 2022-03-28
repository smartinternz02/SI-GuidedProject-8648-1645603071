import numpy as np
import pandas as pd
import os
import joblib
from flask import Flask, jsonify, request, render_template, url_for, redirect, Markup
import requests

app = Flask(__name__)
#joblib_file = "model.pkl"
#model = joblib.load(joblib_file)

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "cqK5NtJb8I1t1_pWgwU2tzWlC7QannwlTTC7NdDk5pX7"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

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

            # NOTE: manually define and pass the array(s) of values to be scored in the next line


            payload_scoring = {"input_data": [{"fields": [
                ["Diagnosis", "FEV1", "Age", "Performance", "Tumor_Size", "Haemoptysis", "Pain", "Dyspnoea", "Cough",
                 "Weakness", "Diabetes_Mellitus", "MI_6mo", "PAD", "Smoking", "Asthma"]],
                             "values": total}]}

            response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9c45902b-d4cf-45fb-b20a-3b8fff63204a/predictions?version=2022-03-25', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
            print("Scoring response")
            print(response_scoring.json())
            predictions = response_scoring.json()
            print(predictions)

            pred = response_scoring.json()

            prediction = pred['predictions'][0]['values'][0][0]

            #prediction = model.predict(total)
            
            #input_variables = pd.DataFrame([[performance, dys, cough, tnm, dm]], columns=['Performance', 'Dyspnoea', 'Cough', 'TNM', 'DM'], dtype=float)

            #prediction = model.predict(total)[0]

            if int(prediction) == 1:
                prediction = "Patient is at High Risk"
               
                
            else:
                prediction = "Patient is Not at Risk"
                
            
            return render_template("result.html", prediction = prediction)
    
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=False)


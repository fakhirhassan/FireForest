import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify , render_template

application = Flask(__name__)
app = application
ridge_model = pickle.load(open('models/ridge_model.pkl' , 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        DC = float(request.form.get('DC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        scalerd_data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC,DC, ISI, Classes, Region]])
        result = ridge_model.predict(scalerd_data)

        return render_template('home.html', results=result[0])
    else:
        return render_template('home.html')

if __name__ == "__main__":

    app.run(debug=True)
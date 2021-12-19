from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        crim = int(request.form['crim'])
        zn=float(request.form['zn'])
        indus=int(request.form['indus'])
        
        chas=int(request.form['chas'])
        nox=int(request.form['nox'])
        rm=int(request.form['rm'])
        age=int(request.form['age'])
        dis=int(request.form['dis'])
        rad=int(request.form['rad'])
        tax=int(request.form['tax'])
        ptratio=int(request.form['ptratio'])
        black=int(request.form['black'])
        lstat=int(request.form['lstat'])





        
        prediction=model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,black,lstat]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this house")
        else:
            return render_template('index.html',prediction_text="the predicted price is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


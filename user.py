import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from math import log10
import pandas
import json


from flask import Flask, request, jsonify, render_template

app = Flask(__name__,static_url_path='/templates/')
class Log(BaseEstimator, TransformerMixin):
    def __init__(self):
        return 
    def fit(self, X, y = None):
        return self
    
    def transform(self, x):
        for i in range(len(x)):
            x[i][0]=log10(x[i][0])
        return x
final_model_reloaded = joblib.load("./model/model.pkl")
req = pandas.DataFrame({
    'meter':200,
    'district':'bagh-feyz',
    'elevator':1,
    'space':1,
    'rooms':1,
    'floor':3,
    'parking':1,
    'buildYear':1390
},index=[2838])
with open('avgByDistrict.json','r') as f:
    districts=json.loads(f.read())
def predictor(r):
    # print(r['district']) 
    r['averageDistrictValue']=r['district'].map(districts)/1e6
    r['test']=r['averageDistrictValue']*r['meter']/1e3
    # print(r['averageDistrictValue'])
    predictions = final_model_reloaded.predict(r)
    return round(predictions[0],2)
print(predictor(req))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Preprocess data if necessary
    req = pandas.DataFrame(data,index=[1])
    prediction = predictor(req)
    return jsonify({'prediction': prediction.tolist()})
@app.route('/', methods=['GET'])
def main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
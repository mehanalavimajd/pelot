import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from math import log10
import pandas
import json
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
    'meter':78,
    'district':'sadeghiyeh',
    'elevator':0,
    'space':1,
    'rooms':2,
    'floor':4,
    'parking':1,
    'buildYear':1379
},index=[2838])
with open('avgByDistrict.json','r') as f:
    districts=json.loads(f.read())
    print(type(districts))
   
print(req['district']) 
req['averageDistrictValue']=req['district'].map(districts)/1e6
req['test']=req['averageDistrictValue']*req['meter']/1e3

print(req['averageDistrictValue'])


predictions = final_model_reloaded.predict(req)
print(predictions)
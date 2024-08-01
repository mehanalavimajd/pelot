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

req = pandas.read_csv("user.csv") # new data
with open('avgByDistrict.json','r') as f:
    districts=json.loads(f.read())
    print(type(districts))
req['averageDistrictValue']=districts.req['district']
req['test']=req['averageDistrictValue']*req['meter']

predictions = final_model_reloaded.predict(req)
print(predictions)
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from math import log10
import pandas
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
d=pandas.read_csv("data3.csv")
new_data = pandas.read_csv("data3.csv") # new data
predictions = final_model_reloaded.predict(new_data)
print(predictions)
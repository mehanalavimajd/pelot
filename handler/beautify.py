'''
what this code will do:
pre-pre-processing the data in data_raw.csv and changing all persian numbers to english
'''

import pandas as pd
import numpy as np
from utils import persianNumber,floorNumber,boolHandler
from averageDistrictValue import averagePriceValue
print('in and out:')
a=input()
b=input()
c=input()

df = pd.read_csv('./'+a)
# print(df)
if(c=='1'):
    df['price'] = df['price'].map(persianNumber)
    df['rooms'] = df['rooms'].map(persianNumber)
    df['meter'] = df['meter'].map(persianNumber)
    df['buildYear'] = df['buildYear'].map(persianNumber)
    df['floor'] = df['floor'].map(floorNumber)
    df['elevator'] = df['elevator'].map(boolHandler)
    df['space'] = df['space'].map(boolHandler)
    df['parking'] = df['parking'].map(boolHandler)
    df=df.drop_duplicates()
    df.sort_values('district')
    df=averagePriceValue(df)
else:
    df=df.drop_duplicates()
    df=df[(df['price'] > 2e9) & (df['price'] < 100e9)]
    df.sort_values('district')
    df=averagePriceValue(df)
df.to_csv("./"+b,index=False)
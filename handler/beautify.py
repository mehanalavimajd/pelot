'''
what this code will do:
pre-pre-processing the data in data_raw.csv and changing all persian numbers to english
'''

import pandas as pd
import numpy as np
from utils import persianNumber,floorNumber,boolHandler
from averageDistrictValue import averagePriceValue
df = pd.read_csv('./data_raw.csv')
print(df)
df['price'] = df['price'].map(persianNumber)
df['rooms'] = df['rooms'].map(persianNumber)
df['meter'] = df['meter'].map(persianNumber)
df['buildYear'] = df['buildYear'].map(persianNumber)
df['floor'] = df['floor'].map(floorNumber)
df['elevator'] = df['elevator'].map(boolHandler)
df['space'] = df['space'].map(boolHandler)
df['parking'] = df['parking'].map(boolHandler)
df=df.drop_duplicates()
df=averagePriceValue(df)
df.to_csv("data.csv",index=False)
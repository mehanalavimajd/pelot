'''
what this code will do:
pre-pre-processing the data in data_raw.csv and changing all persian numbers to english
'''

import pandas as pd
import numpy as np
from utils import persianNumber,floorNumber
df = pd.read_csv('scrape/data_raw.csv')

df['price'] = df['price'].map(persianNumber)
df['rooms'] = df['rooms'].map(persianNumber)
df['meter'] = df['meter'].map(persianNumber)
df['buildYear'] = df['buildYear'].map(persianNumber)
df['floor'] = df['floor'].map(floorNumber)
df=df.drop_duplicates()
df.to_csv("data.csv",index=False)
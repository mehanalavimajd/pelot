import pandas as pd
df=pd.read_csv("data.csv")
districts=[]# name: repeat count
for index,row in df.iterrows():
    if(not row['district'] in districts):
        districts.append(row['district'])
        
print(districts)
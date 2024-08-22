import pandas as pd
df=pd.read_csv("data2.csv")
districts=[]# name: repeat count
for index,row in df.iterrows():
    if(not row['district'] in districts):
        districts.append(row['district'])
districts=sorted(districts)
print(districts)
with open("district.txt",'w') as f:
    for i in districts:
        f.write(f'<option value="{i}">{i}</option>\n')
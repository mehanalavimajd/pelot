import requests
import json
import time,math
from utils import padDictList
from data import dataClassifier
import pandas as pd

Data = {
    'district':[],
    'meter':[],
    'buildYear':[],
    'rooms':[],
    'price':[],
    'floor':[],
    'elevator':[],
    'space':[],
    'parking':[]
}


for j in range(1,30):
    print(j,'stat')
    a = requests.post("https://api.divar.ir/v8/web-search/1/apartment-sell", json.dumps({
    "page": j,
    "json_schema": {
        "category": {
        "value": "apartment-sell"
        }
    },
    "last-post-date": math.floor(time.time()*1000000)
    }))
    result2 = json.loads(a.text)
    tokens = result2['server_action_log']['tokens_info']
    
    for i in range(len(tokens)):

        token = tokens[i]['token']
        
        b = requests.get("https://api.divar.ir/v8/posts-v2/web/"+token)
        # print(b.text)
        print('sleep done')
        try:
            result=json.loads(b.text)
        except:
            print('wait...')
            time.sleep(3)
            b = requests.get("https://api.divar.ir/v8/posts-v2/web/"+token)
            
        dataArray=dataClassifier(result)
        
        Data['buildYear'].append(dataArray[0])
        Data['rooms'].append(dataArray[1])
        Data['price'].append(dataArray[2])
        Data['elevator'].append(dataArray[3])
        Data['space'].append(dataArray[4])
        Data['parking'].append(dataArray[5])
        Data['district'].append(dataArray[6])
        Data['meter'].append(dataArray[7])
    print(f'page {j} done',len(Data['price']))
    
    Data = padDictList(Data, None) # making same length if anything is missed

    df=pd.DataFrame(Data) 
    df.to_csv("data.csv", sep=',', index=False)
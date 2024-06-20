import requests
import json
import time,math
from utils import persianNumber,floorNumber
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
        time.sleep(0.2)
        
        token = tokens[i]['token']
        
        b = requests.get("https://api.divar.ir/v8/posts-v2/web/"+token)
        # print(b.text)
        print('sleep done')
        try:
            result=json.loads(b.text)
        except:
            time.sleep(3)
            b = requests.get("https://api.divar.ir/v8/posts-v2/web/"+token)
            
        district=result['webengage']['district']
        meter=persianNumber(result['sections'][-1]['widgets'][0]['data']['items'][0]['value'])
        buildYear=persianNumber(result['sections'][-1]['widgets'][0]['data']['items'][1]['value'])
        rooms=persianNumber(result['sections'][-1]['widgets'][0]['data']['items'][2]['value'])
        price=persianNumber(result['sections'][-1]['widgets'][1]['data']['value'])
        floor=None
        for i in range(10):
                try:
                    floor=result['sections'][-1]['widgets'][i]['data']['title']
                    if floor=='طبقه':
                        floor=floorNumber(result['sections'][-1]['widgets'][i]['data']['value'])
                        break
                except:
                    pass
        elevator,space,parking = True,True,True
        group={}
        for i in range(10):
                try:
                    group=result['sections'][-1]['widgets'][i]['widget_type']
                    if group=='GROUP_FEATURE_ROW':
                        group=result['sections'][-1]['widgets'][i]['data']['items']
                        break
                except:
                    pass
        
        if 'ندارد' in group[0]['title']:
            elevator=False
        if 'ندارد' in group[1]['title']:
            space=False
        if 'ندارد' in group[2]['title']:
            parking=False
        
        Data['buildYear'].append(buildYear)
        Data['rooms'].append(rooms)
        Data['price'].append(price)
        Data['elevator'].append(elevator)
        Data['space'].append(space)
        Data['parking'].append(parking)
        Data['district'].append(district)
        Data['meter'].append(meter)
    print(f'page {j} done',len(Data['price']))
    def pad_dict_list(dict_list, padel):
        lmax = 0
        for lname in dict_list.keys():
            lmax = max(lmax, len(dict_list[lname]))
        for lname in dict_list.keys():
            ll = len(dict_list[lname])
            if  ll < lmax:
                dict_list[lname] += [padel] * (lmax - ll)
        return dict_list

    Data = pad_dict_list(Data, None) # making same length if anything is missed

    df=pd.DataFrame(Data) 
    df.to_csv("data.csv", sep=',', index=False)
'''
what this code will do:
handling the district by finding average price per m2 and adding it to row
'''

import numpy as np 

def reject_outliers(data, m=3):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / (mdev if mdev else 1.)
    return data[s < m].tolist()


import pandas as pd
# df = pd.read_csv('./data.csv')
def averagePriceValue(df):
    d=df.to_dict('record')
    for i in range(len(d)):
        if(not d[i]['price'] == 0):
            d[i]['pricePerM2']=d[i]['price']/d[i]['meter']
    average={}
    tedad={}
    for i in range(len(d)):
        if('pricePerM2' in d[i]):
            
            district=d[i]['district']
            if(district in average):
                average[district].append(d[i]['pricePerM2'])
                tedad[district]+=1

            else:
                tedad[district]=1
                average[district]=[]
                average[district].append(d[i]['pricePerM2'])
    used=[]
    priceByDistrictDict={}
    for i in range(len(d)):
        district=d[i]['district']
        if(district not in used):
            used.append(district)
            l = np.array(average[district])
            l = reject_outliers(l,m=3)
            average[district] = sum(l)/len(l)
            priceByDistrictDict[district]=average[district]
            print(len(l),tedad[district],average[district])
    for i in range(len(d)):
        district=d[i]['district']
        d[i]['averageDistrictValue']=average[district]
        d[i]['test']=d[i]['meter']*average[d[i]['district']]
    with open('avgByDistrict.json','w') as f:
        import json
        f.write(json.dumps(priceByDistrictDict))
    d=pd.DataFrame(d)
    d=d.drop("pricePerM2",axis=1)
    d.sort_values("district")
    return d

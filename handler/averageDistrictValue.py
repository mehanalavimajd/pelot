'''
what this code will do:
handling the district by finding average price per m2 and adding it to row
'''

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
                average[district]+=(d[i]['pricePerM2'])
                tedad[district]+=1

            else:
                tedad[district]=1
                average[district]=d[i]['pricePerM2']
    used=[]
    for i in range(len(d)):
        district=d[i]['district']
        if(district not in used):
            used.append(district)
            print((average[district]/tedad[district])/1e9)
            average[district]/=tedad[district]

    for i in range(len(d)):
        d[i]['averageDistrictValue']=average[d[i]['district']]
        d[i]['test']=d[i]['meter']*average[d[i]['district']]

    d=pd.DataFrame(d)
    d=d.drop("pricePerM2",axis=1)
    print(average)
    return d

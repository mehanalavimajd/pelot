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
    for i in range(len(d)):
        if('pricePerM2' in d[i]):
            district=d[i]['district']
            if(district in average):
                average[district]+=(d[i]['pricePerM2'])
                average[district]/=2
            else:
                average[district]=d[i]['pricePerM2']
    for i in range(len(d)):
        d[i]['averageDistrictValue']=average[d[i]['district']]

    d=pd.DataFrame(d)
    d=d.drop("pricePerM2",axis=1)
    print(average)
    return d

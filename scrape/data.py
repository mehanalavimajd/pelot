from beautify.utils import persianNumber,floorNumber
def dataClassifier(result):
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
    return [buildYear,rooms,price,elevator,space,parking,district,meter]
def persianNumber(string):
    string=str(string)
    string=string.rstrip("تومان")
    s2=""
    for i in string:
        if i!=',': 
            if i=='۱': s2+='1'
            elif i=='۲': s2+='2'
            elif i=='۳': s2+='3'
            elif i=='۴': s2+='4'
            elif i=='۵': s2+='5'
            elif i=='۶': s2+='6'
            elif i=='۷': s2+='7'
            elif i=='۸': s2+='8'
            elif i=='۹': s2+='9'
            elif i=='۰': s2+='0'        
    return s2

def floorNumber(s):
    i=0
    s2=""
    for i in range(len(s)):
        if s[i]=='۱': s2+='1'
        elif s[i]=='۲': s2+='2'
        elif s[i]=='۳': s2+='3'
        elif s[i]=='۴': s2+='4'
        elif s[i]=='۵': s2+='5'
        elif s[i]=='۶': s2+='6'
        elif s[i]=='۷': s2+='7'
        elif s[i]=='۸': s2+='8'
        elif s[i]=='۹': s2+='9'
        elif s[i]=='۰': s2+='0'  
        else: break
        # bro use switch
    return s2
        
def padDictList(dict_list, padel):
        lmax = 0
        for lname in dict_list.keys():
            lmax = max(lmax, len(dict_list[lname]))
        for lname in dict_list.keys():
            ll = len(dict_list[lname])
            if  ll < lmax:
                dict_list[lname] += [padel] * (lmax - ll)
        return dict_list
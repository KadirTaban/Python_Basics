_dict = {'k1':1,'k2':2 ,'k3':3}


for x in _dict:
    print(x)

for x in _dict:
    print(_dict[x])

for x in _dict.values():
    print(x)

for key,value in _dict.items():
    print(key,value)
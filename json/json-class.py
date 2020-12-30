class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

p1=product("Samsung S10",5000)
p2=product("Samsung S11",6000)
products = [p1.__dict__,p2.__dict__]

import json

with open("urun.json","w") as file:
    json.dump(products,file)

with open("urun.json") as file:
    data = json.load(file)

urunler=[]

for p in data:
    urunler.append(product(p["name"],p["price"]))



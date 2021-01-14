class ogrenci:
    #method
    #atribute
    pass
#object , Instance
ogrenci1 = ogrenci()
ogrenci2 = ogrenci()
#print(type(ogrenci))
#print(ogrenci1,ogrenci2)

class Product:
    pass

p1 = Product() #Samsung S10
p2 = Product() #Samsung A50
p3 = Product() #Iphone 12 Pro

products = [p1,p2,p3]
for p in products:
    print(p)
    print(type(p))
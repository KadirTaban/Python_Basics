class Product:
    def __init__(self, name, price, isActive=False):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Product nesnesi oluşturuldu")
p1 = Product("Samsung S10",5000,True)
p2 = Product("Iphone 12",8000)

print(p1.name,p1.price,p1.isActive)
print(p1.name, p2.price,p2.isActive)
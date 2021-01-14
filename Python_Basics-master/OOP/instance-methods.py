class Person:

    #yapıcı methodlar(constructor)
    def __init__(self,name,surname,year):
        #object attributes
        self.name = name
        self.surname= surname
        self.year = year
    #instance method
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}"
    def calculate_age(self):
        return f"{2021-self.year}"
#object, Instance
p1 = Person("Kadir","Taban",2001)
p2 = Person("Ömer","Taban",1993)

print(p1.intro())
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())
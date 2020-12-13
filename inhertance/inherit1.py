class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

        print("person nesnesi üretildi")
    def intro(self):
        print(self.name,self.surname,self.age)
class Student(Person):

    def __init__(self, name, surname, age,number):
        Person.__init__(self,name,surname,age)
        self.number=number
        print("student nesnesi türetildi")
    def study(self):
        print("{} öğrencisi ders çalışıyor".format(self.number))
class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        Person.__init__(self,name,surname,age)
        self.branch=branch
        print("teacher nesnesi türetildi")

    def teach(self):
        print("{} isimli öğretmen {} dersi veriyor.".format(self.name,self.branch))
p1= Teacher("Ahmet","Turan",20,"math")
p1.intro()
print(p1.branch)
p1.teach()
s1=Student("Ali","Yılmaz",25,4589656)
print(s1.number)
s1.intro()
s1.study()

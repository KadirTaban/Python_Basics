import sqlite3
con=sqlite3.connect("student.db")
cursor = con.cursor()

class Student:
    def __init__(self,ad,soyad,note):
        self.ad=ad
        self.soyad=soyad
        self.note = note

    def veri_ekle2(self):
        cursor.execute("insert into informations values (?,?,?)",(self.ad,self.soyad,self.note))
        con.commit()
Kadir = Student("ömer","taban",7)
Kadir.veri_ekle2()
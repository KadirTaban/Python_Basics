import sqlite3
con=sqlite3.connect("student.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS informations(ogradı TEXT,ogrsoyadı TEXT,note INT )")
def verileri_ekle(ogradı,ogrsoyadı,note):
    cursor.execute("insert into informations values (?,?,?)",(ogradı,ogrsoyadı,note))
    con.commit()


list=[]

while True:
    ogradı=input("Ad: ")
    ogrsoyadı=input("Soyad: ")
    note=int(input("Notu kaç ? "))
    list.append((ogradı,ogrsoyadı,note))
    verileri_ekle(ogradı,ogrsoyadı,note)
    cont= input("Diğer öğrenci için C/S =>")
    if cont=='S':
        print("kayıtlar veritabanına aktarılıyor.")
        print(list)
        break
import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE urunler(isim TEXT,Yazar TEXT,sayfa INT) ")
    con.commit()
def veri_ekle():
    cursor.execute("insert into urunler Values ('İstanbul Hatırası','Ahmet Ümit',561)")
    con.commit()
def veri_ekle2(isim,Yazar,sayfa):
    cursor.execute("insert into urunler values (?,?,?)",(isim,Yazar,sayfa))
    con.commit()
    try:
        con.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen id: {cursor.lastrowid}')
    except ValueError:
        print('hata:')





list=[]
while True:
    isim = input("isim giriniz: ")
    Yazar =input("yazarı kimdir ? ")
    sayfa =int(input("sayfa sayısı kaçtır ?"))
    list.append((isim,Yazar,sayfa))
    veri_ekle2(isim,Yazar,sayfa)
    result = input("devam etmek istiyor musunuz ?(Y/N)")
    if (result =='N' or result=='n'):
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        print(f'{len(list)} tane kayıt eklendi')
        break


"""
def insertProduct(name, price,imageUrl,description):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)
    cursor.execute(sql,values)
    connection.commit()

name=input("ürün adı:")
price = float(input("ürün fiyatı: "))
imageUrl=input("ürün resim adı:")
description = input("ürün açıklaması: ")
insertProduct(name,price,imageUrl,description)
"""
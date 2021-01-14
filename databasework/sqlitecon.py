import sqlite3 # modülümüzü dahil ediyoruz
con = sqlite3.connect("test.db") #kütüphane db ye bağlanıyoruz
cursor = con.cursor()# cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")  # Sorguyu çalıştırıyoruz.
    con.commit()#sorgunun veritabanı üzerinde geçerli olması için
tablo_olustur()
con.close()
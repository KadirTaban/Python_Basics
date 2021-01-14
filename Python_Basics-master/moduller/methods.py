import moduller.db
def ekle(urunAdi,fiyat):
    moduller.db.urunler.append({
        "id":len(moduller.db.urunler) + 1 ,
        "urunAdi":urunAdi,
        "fiyat":fiyat
    })
def güncelle(id,urunAdi,fiyat):
    for urun in moduller.db.urunler:
        if(urun["id"] == id):
            urun["urunAdi"]=urunAdi
            urun["fiyat"] = fiyat
            break
def urunleriGetir():
    for urun in moduller.db.urunler:
        print(f"id{urun['id']} ürün adı : {urun['urunAdi']}fiyat:{urun['fiyat']}")



def urun_ekle(ad,fiyat):
    with open("urunler.txt","a",encoding="UTF-8") as file:
        file.write(f"{ad} fiyat: {fiyat}")

#urun_ekle("samsung s10",5000)


def bul_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate(5)
bul_degistir("urunler.txt","samsung s10","Samsung S9")
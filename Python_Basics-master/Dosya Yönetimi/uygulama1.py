"""
def dosya_kopyala(dosya_adı,yeni_dosya):
    with open(dosya_adı,"r",encoding="UTF-8") as f:
        a=f.read()

    with open(yeni_dosya,"w",encoding="UTF-8") as new_file:
        new_file.write(a)

dosya_kopyala("msg.txt","kopya.txt")
"""
"""
def ters_cevir(dosya_adi,yeni_dosya):
    with open(dosya_adi,"r",encoding="UTF-8") as f:
        a= f.read()
    with open(yeni_dosya,"w",encoding="UTF-8") as new_file:
        new_file.write(a[::-1])

ters_cevir("markalar.txt","ters.txt")
"""
def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar=file.readlines()


    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi":sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi":sum(len(satir) for satir in satirlar)
    }
    return sonuc

print(bilgilendir("msg.txt"))
print(bilgilendir("newfile.txt"))


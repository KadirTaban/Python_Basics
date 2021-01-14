i= 0
adet=int(input("Bir sayı giriniz :"))
urun=[]
a=0

while(i<adet):
    urun_Adı=input("Ürün adı giriniz :")
    fiyat=input("Ürün fiyatı giriniz:")
    urun.append({
     'urun_Adı':urun_Adı,
     'fiyat':fiyat,
    })
    i+=1
#print(urun)
    #for urn in urun:
     #   print(f"Ürün adı:{urun['urun_Adı']} ürün fiyatı:{urn['fiyat']}")
while(a < len(urun)):
    print(f"ürünadı: {urun[a]['urun_Adı']} ürün fiyatı: {urun[a]['fiyat']}")
    a+=1
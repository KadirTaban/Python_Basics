import json
def user(urun_Adi,price,source):
  urun={
      "urun: ":urun_Adi,
      "price: ":price,
      "kaynak: ":source,
  }
  with open("urun.json","w") as file:
      json.dump(urun,file)
user("kitap",500,"a")

def urungetir():
    import json
    with open("urun.json","r") as file:
        urunler=json.load(file)

    print(f'ürün adı: {urunler["urun"]} fiyat: {urunler["price"]}')

urungetir()
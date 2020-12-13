from random import shuffle
class Kart:
    def __init__(self,tip,deger):
        #instance attributes
        self.tip = tip
        self.deger = deger

    def __repr__(self):

        return f" {self.tip} {self.deger}"


class Deste:

    tipler = ["karo","sinek","kupa","maça"]

    degerler= ["a","2","3","4","5","6","7","8","9","10","J","Q","K"]


    def __init__(self):

        self.kartlar=[Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]
    def __iter__(self):
        #return self
        return  iter(self.kartlar)

    def kartSayisi(self):
        return len(self.kartlar)
    def kartlarKaristir(self):
        if(self.kartSayisi()<52):
            return ValueError("Deste bozulmadan kart karıştırabilirsiniz.")
        shuffle(self.kartlar)
    def kartDagit(self,adet):
        kartSayisi=self.kartSayisi()
        adet=min([kartSayisi,adet])
        if kartSayisi==0:
            raise ValueError("Bütün kartlar dağıtıldı")
        adet = min([kartSayisi,adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar=self.kartlar[:-adet]
        repr(kartlar)
    def kartAt(self):
        return self.kartDagit(1)
destek=Deste()
for kart in destek.kartlar:

    print(kart)
#destek.kartlarKaristir()
#destek.kartDagit(15)
#destek.kartlarKaristir()
#print(destek.kartlar)
#print(len(destek.kartlar))
#print(destek.kartSayisi())

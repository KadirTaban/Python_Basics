class sınıf:

    def __init__(self,name,year,mark):
        self.name = name
        self.year = year
        self.mark = mark

    def kisi(self):
        return f"adı {self.name} doğum yılı {self.year} sınav notu :{self.mark} "
s1 = sınıf("kadir",2000,85)
s2 = sınıf("sare",2020,100)

print(s1.kisi())
print(s2.kisi())
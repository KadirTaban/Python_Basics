#sayılar=[1,2,3,4,5]

#sonuc=[i**2 for i in sayılar]
#print(sonuc)


sayilar=[1,4,5,8,9]
sonuc = []

for sayi in sayilar:
   if(sayi % 2 == 0):
        sonuc.append(sayi)
sonuc = [sayi for sayi in sayilar if sayi%2==0]

print(sonuc)

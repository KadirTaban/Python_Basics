import random

hak=5
puan=0
a = random.randint(1, 100)
while hak>0:
    hak-=1
    puan=100 - (5-(hak))*(20)

    tahmin=int(input("Tahmin: "))
    print(a)
    if(tahmin==a):

        print("Tebrikler, kalan hak {} puanın {}".format(hak,puan))
        break

    elif(tahmin<a):

        print("sayıyı büyültün")

    elif(tahmin>a):

        print("sayıyı küçültün.")
    if hak == 0:
        print("hakkınız sona erdi.")


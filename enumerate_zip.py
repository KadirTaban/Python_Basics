a = int(input("asal sayı giriniz: "))

asalmi=True

if(a==1):
    asalmi = False


for i in range(2,a):
    if(a % i == 0 ):
        asalmi=False
        break

if (asalmi==True):
    print("{} ASAL SAYIDIR".format(a))
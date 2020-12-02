a=int(input("Bir büyük değer giriniz: "))
b=int(input("Bir küçük değer giriniz: "))
x=0
while True:
    if(a>b):
        b=b+1
        if(b%2==1) :
            print(b)

bakiye=0
cikis="q"
kart_numarası= int(input("Kart Numarası giriniz: "))
kart_sifre = int(input("Şifreniz: "))
print(bakiye)

if (kart_numarası==000000 and kart_sifre==00):
    a = input("""opsiyonları seçiniz 
            Çıkmak için : q
            para yatırma : b
            para çekme : c

            """)

    while True:

        if(a=="q"):
            break


        elif(a=="b"):

            b=int(input("yatırılacak miktar :"))
            bakiye+=b

            print("yeni bakiye :",bakiye)

            if(b==0):
                a = input("""opsiyonları seçiniz 
                        Çıkmak için : q
                        para yatırma : b
                        para çekme : c

                        """)


        elif(a=="c"):
            c=int(input("Çekilecek miktar :"))
            bakiye-=c

            print((bakiye))
            if (c == 0):
                a = input("""opsiyonları seçiniz 
                                    Çıkmak için : q
                                    para yatırma : b
                                    para çekme : c

                                    """)

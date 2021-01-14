#liste =["1","2","5a","10b","abc","10","50"]

#for x in liste:
 #   try:
  #      sonuc = int(x)
   #     print(x)

    #except ValueError:
     #   print("bu int değil")
      #  continue

while True:
    ilk_sayi = input("ilk sayı(Programdan çıkmak için q ya basınız): ")
    if (ilk_sayi =="q"):
        break

    ikinci_sayi =input("ikinci sayı :")

    try:
        sayi1=int(ilk_sayi)
        sayi2 =int(ikinci_sayi)
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    except(ValueError,ZeroDivisionError):
        print("Bir hata oluştu")
        print("lütfen  tekrar deneyin")
        continue
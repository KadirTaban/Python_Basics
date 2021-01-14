#def tekrarla(txt,adet):
 #   print(txt*adet)

#tekrarla("merhaba\n",5)

#def hesapla(kisa,uzun):
 #   alan=kisa*uzun
  #  cevre=(kisa+uzun)*2
   # print(f'çevre{cevre},alan{alan}')
#hesapla(5,7)
#def yt():
 #   import random
   # a=random.random()
    #print(a)
    #if (a<0.5):
      #  print("Yazi")

  #  else:
   #print("Tura")
#yt()

#def asalmi(x,y):
 #   for a in range(x,y+1):
   #     if (a>1):
    #        for i in range(2,a):
     #           if(a%i ==0):
      #              break
    #     else:
     #           print(a)


#asalmi(5,9)

def tamBolenleribul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleribul(15))
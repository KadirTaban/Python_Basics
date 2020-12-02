#def karsilastirma(a,b):
 #   if(a>b):
  #      return "a b den büyük"
   # elif(b>a):
    #    return "b a dan büyük"
    #else:
     #   return "bunlar eşit"

#sonuc = karsilastirma(4,6)
#print(sonuc)

#def karaktersayisibul(string):
 #   return {letter: string.count(letter) for letter in string}
#sonuc = karaktersayisibul("flutter")
#print(sonuc)

#def update_list(liste,command,position,value=None):
 #   if(command=="remove" and position=="end"):
     #   return liste.pop()
  #  elif(command=="remove" and position=="beginning"):
    #    return liste.pop(0)
   # elif(command=="append" and position=="end"):
      #  liste.append(value)
      #  return liste
    #elif(command=="append" and position=="beginning"):
     #   liste.insert(0,value)
       # return liste

#sonuc=update_list([1,2,3],"append","end","4")


def contains_blue(*renk):
    if "blue" in renk:
        return True
    return False

sonuc=contains_blue("blue","yellow","red")
sonuc=contains_blue("blue","yellow","red")
print(sonuc)
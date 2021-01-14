ogr_adı=input("Öğrenci adı giriniz :")

ogr_math1=int(input("öğrenci 1. notu giriniz :"))
ogr_math2=int(input("öğrenci 2. notu giriniz :"))
ogr_math3=int(input("öğrenci 3. notu giriniz :"))
math_ort= ogr_math1+ogr_math2+ogr_math3
sonuc=int(math_ort/3)

if sonuc > 85 :
    print("Öğrenci {} notunuz : {} iyi.".format(ogr_adı,sonuc))

elif sonuc < 85 :
    print("Öğrenci {} notunuz {} orta .".format(ogr_adı,sonuc))

elif sonuc > 50 :

    print("Öğrenci : {} notunuz {} orta.".format((ogr_adı,sonuc)))

elif sonuc < 50 :
    print("Öğrenci : {} notunuz : {} kötü".format(ogr_adı,sonuc))


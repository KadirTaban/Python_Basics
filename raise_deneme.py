

def parolakontrol(parola):
    turkce_karakterler="şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

        print('geçerli paraola')

parola = input('parola:')
try:
    parolakontrol(parola)

except TypeError as e :
    print(e)
#commentlenmiş print fonksiyonları fixed olduğu için wrapper ladık
def selamlama(fn):
    def wrapper(ad):
        print("hoş geldiniz.")
        fn(ad)
        print("görüşmek üzere.")
    return wrapper
@selamlama
def gunaydın(ad):
#    print("hoş geldiniz.")
    print("günaydın benim adım "+ad)
#    print("görüşmek üzere.")
@selamlama
def gun(ad):
#    print("hoş geldiniz.")

    print("iyi günler  benim adım "+ad)
#    print("görüşmek üzere.")

gunaydın("kadir")

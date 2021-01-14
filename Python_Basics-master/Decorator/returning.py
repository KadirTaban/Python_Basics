
"""
def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
    return inner
user1= yetki_sorgula("Product Edit")
print(user1("Admin"))

print(user1("User"))
"""
def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpim = 1

        for i in args:
            carpim*=i
        return carpim


    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,7,6))

asd = islem("carpma")
print(asd(4,5,6))
urun = {"urunadi":"samsung s10"}
def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(urun, 'fiyat'))
print(get(urun, 'urunAdi'))
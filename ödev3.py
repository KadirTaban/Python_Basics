urunler =['iphone 1','iphone 2 ','iphone 3','a50']
count= -1
for urun in urunler:
    index = urun.find('iphone')
    if (index>-1):
        count+=1
        print(urunler[count])


from bs4 import BeautifulSoup
with open("index.html") as file:
    html_doc = file.read()
obj=BeautifulSoup(html_doc,"html.parser")

sonuc=obj.prettify()
#sonuc=obj.title.name
sonuc=obj.title.string

sonuc=obj.body
sonuc=obj.h1
sonuc=obj.div

print(sonuc)
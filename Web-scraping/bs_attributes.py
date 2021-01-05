from bs4 import BeautifulSoup
with open("index.html") as file:
    html_doc= file.read()

obj= BeautifulSoup(html_doc,"html.parser")
sonuc= obj.div
sonuc=obj.find('div')
sonuc=obj.find(id='div2')
sonuc=obj.find(id='div3')
print(sonuc)

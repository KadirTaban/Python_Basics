import requests
from bs4 import BeautifulSoup
url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
response = requests.get(url).content
soup=BeautifulSoup(response,"html.parser")
list = soup.find_all("li",{"class":"column"})
for li in list:
    name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")
    oldprice=li.find("div",{"class":"proDetail"}).find_all("del")
    print(oldprice)
import requests
import json
url="https://api.exchangeratesapi.io/latest?base="
sonuc=requests.get(url)
sonuc=json.loads(sonuc.text)
print(sonuc)
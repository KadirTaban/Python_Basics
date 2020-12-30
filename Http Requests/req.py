import requests
import json

response = requests.get("https://newsapi.org/v2/top-headlines?country=tr&apiKey=0a242b59e1eb4d20a854149f9c02ae6a")

sonuc = response
sonuc = type(response)
sonuc = response.status_code
sonuc = response.headers
sonuc = response.headers["Content-Type"]
sonuc = response.url
sonuc = response.encoding
sonuc = response.text
todos = json.loads(response.text)
sonuc = todos[0]["title"]
for item in todos:
    if(item["userId"] == 1):
        print(item)
print(sonuc)
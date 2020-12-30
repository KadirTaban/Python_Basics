import requests
headlines_url="https://newsapi.org/v2/top-headlines"
everything_url="https://newsapi.org/v2/everything"
api_key = "0a242b59e1eb4d20a854149f9c02ae6a"
#response = requests.get(headlines_url, params={
 #   "apikey":api_key,
  #  "country":"tr"})


response = requests.get(everything_url, params={
    "apikey":api_key,
    "q":"futbol",
    "language":"tr",
    "sortBy":"publishedAt"

})
haberler = response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
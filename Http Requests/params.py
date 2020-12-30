import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos",params={
    "userId": 1,
    "completed": "true"
})
liste = response.json()
print(liste[0]["title"])




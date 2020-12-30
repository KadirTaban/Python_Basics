# serialize:Bir nesnenin saklanacak / transfer edilecek(yani biz burada json formatına dönüştürüyoruz) forma dönüştürülme işlemidir

# deserialize

import json

# with open("person.json") as file:
#     data = json.load(file)

# json-string

data = """
    {
        "firstName":"Kadir",
        "lastName":"Taban",
        "hobbies": ["spor","kitap okuma"],
        "age":20,
        "children": [
            {
                "firstName": "Sare",
                "age":1
            }
        ]
    }
    """
data = json.loads(data)

print(data)
print(type(data))
#print(data["firstName"])
#print(data["hobbies"])
#print(data["hobbies"][0])


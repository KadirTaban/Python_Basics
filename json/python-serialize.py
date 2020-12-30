#serialize

import json
person = {
    "firstName":"Kadir",
    "lastName":"Taban",
    "hobbies": ["sport","reading"],
    "age":20,
    "children": [
        {
            "firstName": "Sare",
            "age":3
        }
    ]
}

sonuc = json.dumps(person,indent=3)
print(sonuc)
print(person)
print(type(sonuc))
print(person["age"])
with open("person.json","w") as file:
    #file.write(person) (must be str,not dict)
    json.dump(person,file,indent=2)

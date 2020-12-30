db={
    "users":{
        "kadirtaban":{
            "firstname":"Kadir",
            "lastname":"TABAN"
        },
        "saretaban":{
            "firstName":"SARE",
            "lastName":"TABAN",
        },
    },
    "products":{
        "1":{
            "productName":"IPhone8",
            "price":5000

        },
        "2":{
            "ProductName":"IPhone12",
            "price":8000
        }
    }


}
import json
#with open("db.json","w") as file:
 #   json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json") as file:
     db=json.load(file)

#print(db["users"]["kadirtaban"])
#print(db["products"])
db["products"].update({
    "2":{
            "ProductName":"IPhone12",
            "price":9200
    }
})
with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)
data={

  "kadirtaban":{
    "Username": "KADiR",
    "Surname": "TABAN"
  },
  "saretaban":{
    "Username": "SARE",
    "Surname": "TABAN"
  }
}
import json
with open("users2.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("users2.json") as file:
    users=json.load(file)

print(users["saretaban"])
users["kado"] = {"uname":"kadır"}


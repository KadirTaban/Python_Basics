data =[
    {
        "Username":"KADİR",
        "Surname" : "TABAN",
    },
    {
        "Username": "SARE",
        "Surname": "TABAN",
    },

]
import json
user =[
    {
        "Username": "SARE",
        "Surname": "TABAN",
    },

]
#with open("user.json","w")as file:
 #   json.dump(data,file,indent=2)
#with open("user.json","a")as file:#olan dosyanın aynısından sona ekler.
    #json.dump(data,file,indent=2)
with open("user.json") as file:
    users=json.load(file)
    for user in users:#user users dosyasının üzerinde gezsin
        if user["Username"] =="NE":#eğer NE stringi görürse SARE İle değişsin.
            user["Username"] = "SARE"

#users.remove(users[0]) ilk veri olan kadir taban verisini sildi.

with open("users.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)
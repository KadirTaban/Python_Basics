
with open("newfile.txt","w",encoding="UTF-8") as file:
    file.write("Barış Manço")
    print(file)

with open("newfile.txt",encoding="UTF-8")as file:

    print(file.read())
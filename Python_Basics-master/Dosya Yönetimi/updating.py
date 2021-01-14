"""
with open("markalar.txt","r+") as file:
    file.write("1-Dacia")
    file.read()
    file.write("5-BMW\n")
"""

#with open("markalar.txt","r+",encoding="UTF-8") as file:
 #   markalar = file.read()
 #   markalar = "0-Toyota\n"+markalar
 #   file.seek(0)
  #  file.write(markalar)
"""
with open("markalar.txt","r+",encoding="UTF-8") as file:
    markalar = file.readlines()
    markalar.insert(2,"3-Renault\n")
    file.seek(0)
    for marka in markalar:
        file.write(marka)
"""
with open("markalar.txt") as file:
    print(file.read())


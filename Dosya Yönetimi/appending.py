"""
open (dosya_adi,dosya_erisim modu)
EX: open("msg.txt","r")
"r": Read okuma . Dosya konumda yoksa hata verir.
"w": Yazma modu.
    ** Dosya konumda oluşturur.
    ** Dosya içeriğini siler ve yeniden ekleme yapar.
"a": (append)ekleme. Dosya konumda yoksa oluşturur.
"r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.
"""
with open("msg.txt","r+",encoding="UTF-8") as file :
    file.read()
    file.write("Kadir Taban\n")

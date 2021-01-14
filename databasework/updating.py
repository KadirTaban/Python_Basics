import sqlite3

con = sqlite3.connect("student.db")
cursor = con.cursor()
def updatestudent(oldobj,newobj):

    cursor.execute("Update informations Set ogrsoyadı= ? where ogrsoyadı=? ",(newobj,oldobj))
    con.commit()

#updatestudent("as","taban")

def deletestudent(isim):

    cursor.execute("Delete From informations where ogradı= ? ",(isim,))
    con.commit()

deletestudent("ömer",)
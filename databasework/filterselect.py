import sqlite3

def getproducts():
    con = sqlite3.connect("student.db")
    cursor = con.cursor()
    #cursor.execute("Select * from informations where ogradı= 'kadir'")
    #cursor.execute("Select COUNT(*) from informations ")
    #cursor.execute("Select AVG(note) from informations")
    #cursor.execute("Select SUM(note) from informations")
    #cursor.execute("Select MIN(note) from informations ")
    #cursor.execute("Select ogradı from informations Where note = (8)")
    cursor.execute("Select informations.ogradı,")
    #cursor.execute("Select * from informations where ogradı like '%ir'")
    result=cursor.fetchone()

    print(result)
getproducts()
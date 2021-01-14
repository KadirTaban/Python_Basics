import sqlite3
from csv import DictReader
import csv
conn = sqlite3.connect('databank.db')
cur=conn.cursor()
cur.execute('DROP TABLE IF  EXISTS databank')
cur.execute('''
CREATE TABLE "Databank"(
"reviewID" TEXT,
"documentScore" TEXT,
"documentMag" TEXT,
"sentence.sentiment.score" TEXT,
"sentence.sentiment.magnitude" TEXT,
"sentence.text.content" TEXT,
"userName" TEXT,
"userScore" TEXT,
"thumbsUpCount" TEXT,
"reviewCreatedVersion" TEXT,
"at" TEXT,
"response.language" TEXT
)
''')

with open("databank.csv") as file:
    csv_reader= csv.reader(file,delimiter=',')
    for row in csv_reader:
        print(row)
        reviewID=row[0]
        documentScore=row[1]
        documentMag=row[2]
        sentimentscore=row[3]
        sentimentmagnitude=row[4]
        textcontent=[5]
        userName=row[6]
        userScore=row[7]
        thumbsUpCount=row[8]
        reviewCreatedVersion=row[9]
        at=row[10]
        responselanguage=row[11]

        cur.execute('''INSERT INTO Databank(reviewID,documentScore,documentMag,sentimentscore,sentimentmagnitude,textcontent,userName,userScore,thumbsUpCount,reviewCreatedVersion,at,responselanguage)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',(reviewID,documentScore,documentMag,sentimentscore,sentimentmagnitude,textcontent,userName,userScore,thumbsUpCount,reviewCreatedVersion,at,responselanguage))
        cur.execute('''SELECT * FROM ''')


















        






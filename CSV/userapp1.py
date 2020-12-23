from csv import DictWriter,DictReader
def add_user():
    with open("userapp.csv","a") as file:
        headers=["Name","Surname"]
        csv_writer=DictWriter(file,headers)
        csv_writer.writeheader()
        csv_writer.writerows([
            {
                "Name":"Kadir",
                "Surname":"Taban"
            }
        ])

add_user()
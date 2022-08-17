import mysql.connector


def dbacces():
    print("DB Access module called ")
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

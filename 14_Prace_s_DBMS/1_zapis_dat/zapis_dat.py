import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="app1user",
    password="student",
    database="app1"
)

mycursor = connection.cursor()

sql = "INSERT INTO Death(name, painful) VALUES (%s, %s)"
val = ("hanging", True)

mycursor.execute(sql, val)

connection.commit()

connection.close()
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="app1user",
    password="student"
)

print("Pripojeno")

connection.close()
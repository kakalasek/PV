import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="app1user",
    password="student",
    database="app1"
)

sqlSelectAll = "SELECT * FROM Death;"
sqlSelectCount = "SELECT COUNT(*) FROM Death;"

cursor = connection.cursor()
cursor.execute(sqlSelectAll)
allRecords = cursor.fetchall()

for row in allRecords:
    print(row[0], row[1], row[2], sep=', ')

cursor.execute(sqlSelectCount)
recordCount = cursor.fetchall()

for row in recordCount:
    print(row[0])

connection.close()
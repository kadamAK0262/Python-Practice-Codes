import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

select_query = "SELECT * FROM users"

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
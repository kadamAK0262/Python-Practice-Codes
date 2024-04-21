import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect to MySQL database")

mycursor = connection.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:                 # print all databases in mysql in row.
  print(x)
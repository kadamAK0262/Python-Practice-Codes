import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
user_data = ("akshay_kadam", "akshay@example.com", "kadam")

cursor.execute(insert_query, user_data)

connection.commit()

print("Data inserted successfully")

cursor.close()
connection.close()
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM users LIMIT 3")
    
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    connection.close()
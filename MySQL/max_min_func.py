import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

try:
    cursor.execute("SELECT MIN(amount), MAX(amount) FROM orders")

    result = cursor.fetchone()
    min_amount, max_amount = result
    print("Minimum amount:", min_amount)
    print("Maximum amount:", max_amount)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    connection.close()
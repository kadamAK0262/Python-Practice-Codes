import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

# Using COUNT(), AVG(), and SUM() functions
cursor = connection.cursor()

try:
    
    cursor.execute("SELECT COUNT(*), AVG(amount), SUM(amount) FROM orders")

    result = cursor.fetchone()
    count, avg_amount, total_amount = result
    print("Number of orders:", count)
    print("Average amount:", avg_amount)
    print("Total amount:", total_amount)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    connection.close()
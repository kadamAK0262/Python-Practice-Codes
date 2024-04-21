import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

try:
    cursor.execute("UPDATE users SET password = 'king_in_north' WHERE id = 7")

    connection.commit()

    print("Users record updated.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    connection.close()
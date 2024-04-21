import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)

cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM users WHERE username = 'akshay_kadam' ORDER BY password")

    results = cursor.fetchall()

    print("Users from table sorted by password :")
    for row in results:
        print(row)

    cursor.execute("DELETE FROM users WHERE username = 'white_wolf'")

    connection.commit()

    print("\nusers from username deleted.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    cursor.close()
    connection.close()
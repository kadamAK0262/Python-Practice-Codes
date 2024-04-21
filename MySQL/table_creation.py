import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshay@0262",
    database="python"
)


cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
)
"""

cursor.execute(create_table_query)

print("Table created successfully")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)


cursor.execute("ALTER TABLE users ADD COLUMN password VARCHAR(100)")

connection.commit()

cursor.close()
connection.close()











# connection.commit(): This line is used to commit the changes made to the database. In MySQL, changes made within a transaction 
# are not permanent until they are explicitly committed. By calling connection.commit(), 
# you're indicating to MySQL that you want to make the changes permanent. 
# This is typically done after executing insert, update, or delete queries. If you don't commit the changes, 
# they will be rolled back when the connection is closed.

# cursor.close(): This line is used to close the cursor object. Cursors are used to execute SQL queries and fetch results 
# from the database. Once you're done executing queries and fetching results, it's good practice to close the cursor to release 
# the resources associated with it. This helps in efficient memory management.

# connection.close(): This line is used to close the connection to the database. Once you're done with all database operations 
# and you no longer need the connection, you should close it to release the resources associated with it. This includes closing 
# network connections, releasing memory, and other cleanup tasks. It's important to close the connection properly to avoid resource 
# leaks and to ensure that the connection is released back to the pool for reuse.


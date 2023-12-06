import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("game_database.db")
cursor = connection.cursor()

# cursor.execute("UPDATE Tasks SET NPCID=4 WHERE TaskID=4")

# cursor.execute("INSERT INTO Players VALUES(1,'VASU',300,600,0,'FALSE')")


# Commit the changes
connection.commit()
cursor.execute("UPDATE Players SET status='FALSE' WHERE PlayerID=1")
# Select all data from the 'users' table
cursor.execute("SELECT * FROM Players")
rows = cursor.fetchall()


# Print the results
for row in rows:
    
    print(row)

# Close the connection
connection.close()

import sqlite3

def Task_Desc(Task_id):
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()

    # Use a placeholder (?) in the SQL query and provide the TaskID as a tuple
    cursor.execute("SELECT Description FROM Tasks WHERE TaskID=?", (Task_id,))

    # Fetch the result
    task_description = cursor.fetchone()

    # Commit the changes (not necessary for SELECT queries)
    connection.commit()

    # Print or return the result
    print(task_description)
    return task_description

    # Close the connection
    connection.close()



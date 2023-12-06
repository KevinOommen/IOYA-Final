import random
import sqlite3



def PickTask(player_id):
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()
    random_number = random.randint(1, 4)
    
    cursor.execute("UPDATE Players SET TaskID=? WHERE PlayerID=?", (random_number, player_id))
    connection.commit()
    return random_number
    connection.close()


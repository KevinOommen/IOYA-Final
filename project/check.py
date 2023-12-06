import sqlite3


def check(npc_id, player_id):
    
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()    
    cursor.execute("SELECT TaskID FROM Players WHERE PlayerID=?", (player_id,))
    TaskID = cursor.fetchone() 

    if TaskID:
        TaskID = TaskID[0]  
        cursor.execute("SELECT NPCID FROM Tasks WHERE TaskID=?", (TaskID,))
        NPC_ID = cursor.fetchone() 

        if NPC_ID and npc_id == NPC_ID[0]:
            print("Correct submission")
            return 1
            cursor.execute("UPDATE Players SET status='TRUE' WHERE PlayerID=?",(player_id,))
        else:
            return 0
    else:
        return ("Player not found")

    connection.commit()

    
    connection.close()

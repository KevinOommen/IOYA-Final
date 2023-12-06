import sqlite3

def get_npc_id_by_name(name):
    connection = sqlite3.connect("game_database.db")
    cursor = connection.cursor()

    # Use a placeholder (?) in the SQL query and provide the 'name' as a tuple
    cursor.execute("SELECT NPCID FROM NPCs WHERE LOWER(Name) = LOWER(?);", (name,))

    # Fetch the result
    npc_id_tuple = cursor.fetchone()

    # Close the connection
    connection.close()

    # Return the NPCID or None if no match is found
    return npc_id_tuple[0] if npc_id_tuple else None

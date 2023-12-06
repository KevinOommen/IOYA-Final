import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('game_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create Players Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Players (
        PlayerID INTEGER PRIMARY KEY,
        Username VARCHAR,
        PositionX REAL,
        PositionY REAL,
        TaskID INTEGER,
        Status VARCHAR
    )
''')

# Create NPCs Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS NPCs (
        NPCID INTEGER PRIMARY KEY,
        Name VARCHAR,
        PositionX REAL,
        PositionY REAL,
        Dialogue VARCHAR,
        Sprite VARCHAR
    )
''')

# Create Tasks Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        TaskID INTEGER PRIMARY KEY,
        Title VARCHAR,
        Description VARCHAR,
        Deadline VARCHAR,
        NPCID INTEGER,
        FOREIGN KEY (NPCID) REFERENCES NPCs(NPCID)
    )
''')

# Create Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        PlayerID INTEGER PRIMARY KEY,
        Username VARCHAR UNIQUE,
        PasswordHash VARCHAR,
        Email VARCHAR UNIQUE,
        LastLogin VARCHAR,
        IsActive INTEGER
    )
''')

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

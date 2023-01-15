import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO pages (title,username,tagline,content) VALUES (?, ?, ?, ?)",
            ('Starter title', 'IshanD', 'starter tagline', 'starter text')
            )

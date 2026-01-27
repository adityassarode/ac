import sqlite3

connection = sqlite3.connect('home_automation.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fan TEXT NOT NULL,
    light TEXT NOT NULL,
    door TEXT NOT NULL
)
''')

connection.commit()
connection.close()

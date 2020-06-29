""" Create a simple Password Manager"""

import sqlite3

# create a connection with the database

conn = sqlite3.connect('pwd_manager.db')

c = conn.cursor()

# Create the table


c.execute("""CREATE TABLE passwords
           (id TEXT,
           name TEXT,
            url TEXT,
            username TEXT,
            password TEXT)""")

#c.execute("DROP TABLE passwords")
#conn.commit()
#id INTEGER PRIMARY KEY AUTOINCREMENT,
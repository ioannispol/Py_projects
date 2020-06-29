import sqlite3
import os

conn = sqlite3.connect('pwd_manager.db')
c = conn.cursor()
print(conn)


def search_all():
    conn = sqlite3.connect('pwd_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    result = c.fetchall()
    for rows in result:
        print(rows)

    input("Press Enter to Exit")
    os.system('cls')
    conn.close()
    return

import os
import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('pwd_manager.db')
c = conn.cursor()
print(conn)


def csvToDb():
    conn = sqlite3.connect('pwd_manager.db')
    c = conn.cursor()
    print(conn)
    
    read_inputs = pd.read_csv(r'D:\giann\Documents\docs\input.csv')
    read_inputs.to_sql('passwords', conn, if_exists='append', index=False) # Insert the csv file into the table 'passwords'
    c.execute("""INSERT INTO passwords
                    (name, url, username, password) VALUES
                    (?, ?, ?, ?)
                """)
    conn.commit()
    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")
    conn.commit()
    conn.close()
    print("Your passwords has now been imported")
    input("Press Enter to Exit")
    os.system('cls')
    return
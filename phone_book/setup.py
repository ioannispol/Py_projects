import sqlite3

# create a connection with the db
conn = sqlite3.connect('book.db')

c = conn.cursor()

# create table
c.execute("""CREATE TABLE phonebook
    (id text,
     name text,
     surename text,
     phone_number text,
     email text)
    """)

# commit the changes
conn.commit()
conn.close()

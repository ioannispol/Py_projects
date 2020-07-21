import sqlite3


# connect to db
conn = sqlite3.connect('book.db')
c = conn.cursor()

def new_contact():
    conn = sqlite3.connect('book.db')
    c = conn.cursor()
    # personal info
    name = str(input("Enter Name: "))
    surename = str(input("Enter Surename: "))
    phone = str(input("Enter phone: "))
    email = str(input("Enter email: "))
    c.execute("""INSERT INTO phonebook
        (name, surename, phone, email) VALUES
        (?, ?, ?, ?)
        """, (name, surename, phone, email))

    conn.commit()

    c.execute("""SELECT * FROM phonebook ORDER BY id DESC LIMIT 1""")
    result = c.fetchone()
    for row in result:
        print(row)
    conn.close()
    input("Press Enter to Exit")
    return


import sqlite3

conn = sqlite3.connect('pwd_manager.db')
c = conn.cursor()


def new_pwd():
    conn = sqlite3.connect('pwd_manager.db')
    c = conn.cursor()

    website = input("Enter website: ")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    c.execute("""INSERT INTO passwords
                (website, username, email, password) VALUES
                (?, ?, ?, ?)
            """, (website, username, email, password))
    conn.commit()
    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    for row in result:
        print(row)
    conn.close()
    input("Press Enter to Exit")
    return

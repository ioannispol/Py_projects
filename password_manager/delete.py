import sqlite3
import os


def delete_pwd():
    conn = sqlite3.connect('pwd_manager.db')
    c = conn.cursor()
    print(conn)

    print("\nYou are deleting passwords by website name!")
    user_input = input("Enter id: ")

    c.execute("""DELETE FROM passwords
    WHERE id = ?
    """, (user_input,))
    conn.commit()
    conn.close()
    print("Your password has now been deleted")
    input("Press Enter to Exit")
    os.system('cls')
    return

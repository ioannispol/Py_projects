import sqlite3
import os
import new_password as np
import searchall as sa
import delete
import import_csv as csv

ADMIN_PASSWORD = "admin"

connect = input("Enter your password: \n")

while connect != ADMIN_PASSWORD:
    connect = input("Enter your password: ")
    if connect == 'q':
        break

os.system('cls')

conn = sqlite3.connect('pwd_manager.db')
c = conn.cursor()

while True:
    os.system('cls')

    print("*" * 30)
    print("Welcome to the Password Manager: ")
    print("Commands:")
    print("s = See all passwords")
    print("n = New password")
    print("d = Delete password")
    print("i = Import passwords")
    print("q = Quit")
    print("*" * 30)
    userInput = input("Enter command: ")
    if userInput == 's':
        sa.search_all()
    elif userInput == 'n':
        np.new_pwd()
    elif userInput == 'd':
        delete.delete_pwd()
    # TODO create an option to imput passwords from csv files
    elif userInput == 'i':
        csv.csvToDb()
    elif userInput == 'q':
        break
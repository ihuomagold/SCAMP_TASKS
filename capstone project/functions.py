import sqlite3

# This program is a user management system

# STEP1: Create a Connection To the Database

conn = sqlite3.connect('Students.db')
cursor = conn.cursor()

print('opened successfully')

cursor.execute("""CREATE TABLE STUDENTS (
    first  TEXT(50)            NOT NULL,
    last   TEXT(50)            NOT NULL,
    age         INT                 NOT NULL,
    email       TEXT(50)            NOT NULL,
    course TEXT(50)        NOT NULL,
    reg_no  INT                 NOT NULL
    )""")

cursor.row_factory = sqlite3.Row
conn.commit()
conn.close()


# To Drop/Delete a Table
# cursor.execute("""DROP TABLE STUDENTS""")
# conn.commit()
# conn.close()


def ask():
    try:
        return int(input("Welcome!, Please enter your chosen option:(0 = exit, 1 = add record, 2 = delete record,"
                         " 3 = update record, 4 = show all users): "))
    except ValueError:
        return -1


ask()


def add_users():
    conn = sqlite3.connect('Students.db')

    cursor = conn.cursor()
    # global choice
    # # while choice is not 0:
    # while choice < 0 or choice > 4:
    #     choice = ask()
    # if choice == 1:
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = (input("Enter your email: "))
    course = input("Enter your course of study: ")
    reg_no = int(input("Enter your registration number: "))
    #
    # cursor.execute("SELECT rowid, * FROM STUDENTS")
    # query = cursor.fetchone()                         ### This keeps returning user already exists
    # if query is not None:
    #     print("The user already exists!")
    # else:
    cursor.execute("INSERT INTO STUDENTS VALUES(?,?,?,?,?,?)", (first, last, age, email, course, reg_no))
    print("New user added...")

    conn.commit()
    conn.close()

#
# def add_many():                           ### I'M NOT TOO SURE HOW TO GO ABOUT THIS
#     conn = sqlite3.connect('Students.db')
#
#     cursor = conn.cursor()
#     data = input("Enter details: ")
#
#     # cursor.execute("SELECT rowid, * FROM STUDENTS")
#     # query = cursor.fetchmany()
#     # if query is not None:
#     #     print("The users already exist!")
#     # else:
#     cursor.executemany("INSERT INTO STUDENTS VALUES(?)", data)
#     print("New users added...")
#
#     conn.commit()
#     conn.close()


def delete_record():
    conn = sqlite3.connect('Students.db')

    cursor = conn.cursor()
    identity = input("Enter the id of the record to be deleted: ")
    cursor.execute("DELETE FROM STUDENTS WHERE rowid = (?)", identity)

    print("Deleting Record...")
    print("Done!")
    conn.commit()
    conn.close()


# def update_record():  ### I'm working on this now

import utils
# This program is a user management system
db_name = "students.db"


# CREATE A DATABASE
def create_database():
    cursor = utils.connect_to_database(db_name)

    table_properties = """
    first_name  TEXT(50)            NOT NULL,
    last_name   TEXT(50)            NOT NULL,
    age         INT                 NOT NULL,
    email       TEXT(50)            NOT NULL,
    username    TEXT(10)            NOT NULL,
    course TEXT(50)                 NOT NULL,
    reg_no  INT                     NOT NULL"""

    utils.create_table(cursor, "Users", table_properties)


# SELECT THE FUNCTION TO BE PERFORMED
def ask():
    try:
        return int(input("Enter your chosen option:(1 = add record, 2 = list record, 3 = delete record,"
                         " 4 = update record, 5 = update lastname, 6 = update age, 7 = update email, "
                         "8 = update username, 9 = update course""): "))
    except ValueError:
        return -1


# ADD USERS TO THE DATABASE
def add_users():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    age = int(input("Enter your age: "))
    email = str(input("Enter your email: "))
    username = str(input("Enter your username: "))
    course = input("Enter your course of study: ")
    reg_no = int(input("Enter your registration number: "))

    cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?,?,?)", (first_name, last_name, age, email, username, course,
                                                               reg_no))
    print("New user added...")

    conn.commit()
    conn.close()
#


# READ RECORDS FROM THE DATABASE
def list_all():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM Users")
    lists = cursor.fetchall()

    for item in lists:
        print(item[0], " ", item[1], "\t\t", item[2], "\t\t", item[3], "\t\t", item[4], "\t\t", item[5], "\t\t",
              item[6])

    print("Command Executed successfully...")

    conn.commit()
    conn.close()
#


# DELETE A RECORD FROM THE DATABASE
def delete_record():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    identity = int(input('Enter the user_id to be deleted: '))
    utils.delete_users(cursor, 'Users', identity)

    print("Deleting Record...")
    print("Done!")

    conn.commit()
    conn.close()
#


# UPDATE FIRST NAME
def update_firstname():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    firstname = input("Enter the new firstname: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'firstname', firstname, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()


# UPDATE LASTNAME
def update_lastname():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    lastname = input("Enter the new lastname: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'lastname', lastname, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()


# UPDATE AGE
def update_age():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    age = int(input("Enter the new age: "))
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'age', age, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()


# UPDATE EMAIL
def update_email():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    email = input("Enter the new email: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'firstname', email, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()


# UPDATE USERNAME
def update_username():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    username = input("Enter the new username: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'username', username, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()


# UPDATE COURSE
def update_course():
    conn = utils.connect_to_database(db_name)
    cursor = conn.cursor()

    course = input("Enter the new course: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'course', course, id_)

    print("Updated Successfully...")

    conn.commit()
    conn.close()

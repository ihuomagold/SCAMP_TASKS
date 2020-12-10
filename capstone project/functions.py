import utils
# This program is a user management system


def create_database():
    db_name = "students.db"
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


def ask():
    try:
        return int(input("Enter your chosen option:(1 = add record, 2 = list record, 3 = delete record,"
                         " 4 = update record): "))
    except ValueError:
        return -1


# # while choice is not 0:
# #     while choice < 0 or choice > 3:
# #         choice = ask()
# #
# # print("Welcome!")
#
#
def add_users():
    cursor = utils.connect_to_database("students.db")

    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    age = int(input("Enter your age: "))
    email = str(input("Enter your email: "))
    username = str(input("Enter your username: "))
    course = input("Enter your course of study: ")
    reg_no = int(input("Enter your registration number: "))

    # utils.add_users_to_table(cursor, 'Users', 'first_name, last_name, age, email, username, course, reg_no',
    #                          (first, last, age, email, username, course, reg_no))

    cursor.execute("INSERT INTO Users VALUES(?,?,?,?,?,?,?)", (first_name, last_name, age, email, username, course,
                                                               reg_no))
    print("New user added...")


# #
def list_all():
    cursor = utils.connect_to_database("students.db")
    cursor.execute("SELECT * FROM Users")
    lists = cursor.fetchall()

    for item in lists:
        print(item[0], " ", item[1], "\t\t", item[2], "\t\t", item[3], "\t\t", item[4], "\t\t", item[5], "\t\t",
              item[6])

    print("Command Executed successfully...")
#


def delete_record():
    cursor = utils.connect_to_database("students.db")
    identity = int(input('Enter the user_id to be deleted: '))
    utils.delete_users(cursor, 'Users', identity)
    # identity = input("Enter the id of the record to be deleted: ")
    # cursor.execute("DELETE FROM STUDENTS WHERE rowid = (?)", identity)
    #
    print("Deleting Record...")
    print("Done!")
#


def update_firstname():
    cursor = utils.connect_to_database("students.db")
    firstname = input("Enter the new name: ")
    id_ = input("Enter id: ")
    utils.update_user(cursor, 'Users', 'firstname', firstname, id_)

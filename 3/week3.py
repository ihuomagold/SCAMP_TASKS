import sqlite3

# Create a connection to the Database

conn = sqlite3.connect('class_list.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE students (
    first_name text,
    last_name text,
    reg_no integer
    )""")

# To drop(delete a table)
# c.execute("""DROP TABLE students""")

# Inserting a single value
c.execute("INSERT INTO students VALUES ('Angel', 'Afube', 20151010693 )")

# Inserting multiple values at once
all_students = [
                  ('Ikechukwu', 'Madubuike', 20151018593),
                  ('Ifeanyi', 'Dike', 20151019463),
                  ('Jeremiah', 'Esieboma', 20151019853)
               ]

c.executemany("INSERT INTO students VALUES(?,?,?)", all_students)

# To Query the database
c.execute("SELECT * FROM students")
lists = c.fetchall()

# print("NAME", "\t\t", "REG_NO")
# print("---------------------------")
for item in lists:
    print(item[0], " ", item[1], "\t\t",  item[2])

print("Command Executed successfully...")

# Commit the database
conn.commit()

# Close the connection
conn.close()

import sqlite3


def connect_to_database(db_name):     # This creates a connection to the Database

    conn = sqlite3.connect(db_name)

    return conn


def create_table(cursor, table_name, table_properties):   # Creates a table in the Database
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({table_properties})")


def add_users_to_table(cursor, table_name, columns, values):   # Adds Users to the Database
    cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES({values})")


def delete_users(cursor, table_name, identity):  # Deletes Users from the database
    cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ({identity})")


def update_user(cursor, table_name, columns, values, identity):  # Updates a user record
    cursor.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE rowid = ({identity})")

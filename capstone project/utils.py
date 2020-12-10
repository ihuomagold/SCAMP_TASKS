import sqlite3
# This creates a connection to the Database


def connect_to_database(db_name):

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    return cursor


def create_table(cursor, table_name, table_properties):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({table_properties})")


def add_users_to_table(cursor, table_name, columns, values):
    cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES({values})")


def delete_users(cursor, table_name, identity):
    cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ({identity})")


def update_user(cursor, table_name, columns, values, identity):
    cursor.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE rowid = ({identity})")
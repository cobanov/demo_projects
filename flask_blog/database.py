import sqlite3
import os


def create_tables(table_name):
    with sqlite3.connect("data.db") as connection:
        connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (content TEXT, date TEXT)")


def create_entry(table_name, content, date):
    with sqlite3.connect("data.db") as connection:
        connection.execute(f"INSERT INTO {table_name} VALUES (?, ?)", (content, date))


def retrieve_entries(table_name):
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

def delete():
    os.remove("data.db")
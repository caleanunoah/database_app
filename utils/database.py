"""
concerned with storing and retrieving things from a json file

"""
import json
import sqlite3
from typing import Tuple

database_file = "lib_db.db"


def initialize_file():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer default 0)')
    connection.commit()
    connection.close()
    return


def add_book(name, author):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()
    return books


def mark_as_read(name):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute('DELETE from books WHERE name=?', (name,))
    connection.commit()
    connection.close()

"""
concerned with storing and retrieving things from a json file

"""
import json
from utils.database_connection import DatabaseConnection

database_file = "lib_db.db"

def initialize_file():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer default 0)')


def add_book(name, author):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_as_read(name):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE from books WHERE name=?', (name,))

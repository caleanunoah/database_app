"""
concerned with storing and retrieving things from a json file

"""
import json
from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union

database_file = "lib_db.db"
Book = Dict[str, Union[str, int]]

def initialize_file() -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer default 0)')


def add_book(name, author) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

# Type hinting: list of dictionaries with str keys and a combination of str/int values
def get_all_books() -> List[Book]:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_as_read(name) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name) -> None:
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE from books WHERE name=?', (name,))

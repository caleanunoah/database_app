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
    #new_book = {'name': name, 'author': author, 'read': 0}
    #with open(database_file, 'r') as fp:
    #    books = json.load(fp)
    #books.append(new_book)
    #with open(database_file, 'w') as fp:
    #    json.dump(books, fp)


def get_all_books():
    with open(database_file, 'r') as fp:
        return json.load(fp)


def mark_as_read(name):
    # the following is more readable than mine/
    with open(database_file, 'r') as fp:
        books = json.load(fp)
    for entry in books:
        if entry['name'] == name:
            entry['read'] = 1
    with open(database_file, 'w') as fp:
        json.dump(books, fp)


def delete_book(name):
    with open(database_file, 'r') as fp:
        books = json.load(fp)
    books = [entry for entry in books if entry['name'] != name]
    with open(database_file, 'w') as fp:
        json.dump(books, fp)

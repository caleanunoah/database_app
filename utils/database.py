"""
concerned with storing and retrieving things from a json file

"""
import json

# file with non-empty list of books saved as dictionaries
#   book = {
#           name: str
#           author: str
#           read:   bool
#                       }
database_file = 'utils\database.json'


def initialize_file():
    with open(database_file, "w") as fp:
        json.dump([], fp)


def add_book(name, author):
    new_book = {'name': name, 'author': author, 'read': False}
    with open(database_file, 'r') as fp:
        books = json.load(fp)
    books.append(new_book)
    with open(database_file, 'w') as fp:
        json.dump(books, fp)


def get_all_books():
    with open(database_file, 'r') as fp:
        return json.load(fp)


def mark_as_read(name):
    # the following is more readable than mine
    with open(database_file, 'r') as fp:
        books = json.load(fp)
    for entry in books:
        if entry['name'] == name:
            entry['read'] = True
    with open(database_file, 'w') as fp:
        json.dump(books, fp)


def delete_book(name):
    with open(database_file, 'r') as fp:
        books = json.load(fp)
    books = [entry for entry in books if entry['name'] != name]
    with open(database_file, 'w') as fp:
        json.dump(books, fp)

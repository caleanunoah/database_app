# Using list to store books as dictionaries.  Menu prompts user
import utils.database as database
import sqlite3

USER_CHOICE = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FUNCTIONS FOR MENU PROMPTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# add a book to the database
def prompt_add_book():
    name = input("Enter name: ")
    author = input("Enter author: ")
    database.add_book(name, author)


# print names of book currently in database
def list_books():
    books = database.get_all_books()
    for book in books:
        name = book['name'].capitalize()
        author = book['author'].capitalize()
        read = 'YES' if book['read'] else 'NO'
        print(f"- {name} by {author}. read: {read}.")


# mark a book as read.
def mark_as_read():
    name = input("Enter the book you finished: ")
    database.mark_as_read(name)


# delete a book from the database
def delete_book():
    name = input("Enter name of book you wish to delete: ")
    database.delete_book(name)


# MENU function to take user input and execute appropriate function
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            mark_as_read()
        elif user_input == 'd':
            delete_book()
        else:
            print("IDK what command that is! ")
        user_input = input(USER_CHOICE)

if __name__ == "__main__":
    database.initialize_file()
    menu()

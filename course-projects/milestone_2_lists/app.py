from utils import json_database as database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


# ask for book name and author
def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database.add_book(name, author)


# show all books in our list
def list_books():
    database.get_all_books()


# ask for book name and change it to 'read' in our list
def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_book_as_read(name)


# ask for book name and remove book from list
def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    database.delete_book(name)


operations = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in operations:
            operations[user_input]()
        else:
            print('Unknown command. Please try again!')

        user_input = input(USER_CHOICE)


if __name__ == "__main__":
    menu()

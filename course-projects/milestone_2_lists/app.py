from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        pass


# ask for book name and author
def prompt_add_book():
    ...


# show all books in our list
def list_books():
    ...


# ask for book name and change it to 'read' in our list
def prompt_read_book():
    ...

# ask for book name and remove book from list
def prompt_delete_book():
    ...

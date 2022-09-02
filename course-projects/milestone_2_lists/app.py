from utils import database

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
    name = input('Enter the book name: ')
    author = input('Enter the book author: ')
    database.add_book(name, author)


# show all books in our list
def list_books():
    database.get_all_books()


# ask for book name and change it to 'read' in our list
def prompt_read_book():
    name = input('Enter the book name: ')
    database.mark_as_read(name)


# ask for book name and remove book from list
def prompt_delete_book():
    name = input('Enter the book name: ')
    database.delete_book(name)


operations = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input in operations:
            operations[user_input]()
        else:
            print('Invalid option, please enter again!')

        user_input = input(USER_CHOICE)


if __name__ == "__main__":
    menu()

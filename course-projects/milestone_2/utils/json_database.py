"""
Concerned with storing and retrieving books from a JSON file.
Format of the json file:
[{
    "name": name,
    "author": author,
    "read": false
}]
"""
import json

FILE_NAME = "books.json"


def create_book_table():
    # just to make the file is there
    try:
        with open(FILE_NAME, 'x') as file:
            json.dump([], file)
    except:
        ...


def add_book(name, author):
    books = get_book_from_file()

    books.append({
        'name': name,
        'author': author,
        'read': False
    })

    _save_all_books(books)


def get_book_from_file():
    with open(FILE_NAME, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(FILE_NAME, 'w') as file:
        json.dump(books, file, indent=4)


def get_all_books():
    books = get_book_from_file()
    if books:
        for book in books:
            read = 'YES' if book['read'] else 'NO'
            print(f"{book['name']} by {book['author']}, read: {read}")
    else:
        print('The list of books is empty!')


def mark_book_as_read(book_name):
    books = get_book_from_file()

    if books:
        for book in books:
            if book['name'] == book_name:
                book['read'] = True
        _save_all_books(books)
    else:
        print('The list of books is empty!')


def delete_book(book_name):
    books = get_book_from_file()
    if books:
        books = [book for book in books if book['name'] != book_name]
        _save_all_books(books)
    else:
        print('The list of books is empty!')

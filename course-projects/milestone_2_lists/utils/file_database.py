"""
Concerned with storing and retrieving books from a CSV file.
Format of the csv file:
name,author,read\n
name,author,read\n
name,author,read\n

or
name#author#read
"""

FILE_NAME = "books.txt"


def create_book_table():
    # just to make the file is there
    try:
        with open(FILE_NAME, 'x'):
            pass
    except:
        ...


def add_book(name, author):
    with open(FILE_NAME, 'a') as file:
        file.write(f'{name},{author},0\n')


def get_book_from_file():
    with open(FILE_NAME, 'r') as file:
        # [[name, author, read], [name, author, read], ...]
        lines = [line.strip().split(',')
                 for line in file.readlines()]

    return [
        {
            'name': name,
            'author': author,
            'read': bool(int(read))
        }
        for name, author, read in lines
    ]


def get_all_books():
    books = get_book_from_file()
    if books:
        for book in books:
            read = 'YES' if int(book['read']) else 'NO'
            print(f"{book['name']} by {book['author']}, read: {read}")
    else:
        print('The list of books is empty!')


def _save_all_books(books):
    with open(FILE_NAME, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(book_name):
    books = get_book_from_file()

    if books:
        for book in books:
            if book['name'] == book_name:
                book['read'] = '1'
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

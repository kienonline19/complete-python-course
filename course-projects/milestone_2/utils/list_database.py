"""
Concerned with storing and retrieving books from a list.
Using Python list: in memory database.
A text based application
"""

books = []


def add_book(name, author):
    books.append({
        'name': name,
        'author': author,
        'read': False
    })


def get_all_books():
    if books:
        for book in books:
            read = 'YES' if book['read'] else 'NO'
            print(f"{book['name']} by {book['author']}, read: {read}")
    else:
        print('The list of books is empty!')


def mark_book_as_read(name):
    if books:
        for book in books:
            if book['name'] == name:
                book['read'] = True
    else:
        print('The list of books is empty!')


def delete_book(name):
    global books
    if books:
        books = [book for book in books if book['name'] != name]
    else:
        print('The list of books is empty!')

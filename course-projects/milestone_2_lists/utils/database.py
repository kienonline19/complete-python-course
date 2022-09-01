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

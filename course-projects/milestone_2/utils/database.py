"""
Concerned with storing and retrieving books from a sqlite database.
"""
import sqlite3

FILE_NAME = "data.db"


def create_book_table():
    connection = sqlite3.connect(FILE_NAME)

    cursor = connection.cursor()
    sql_command = """create table if not exists books (
        name text primary key,
        author text,
        read int
    );"""

    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def add_book(name, author):
    conn = sqlite3.connect(FILE_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author))
    
    # SQL Injection
    # author: ', 0); DROP TABLE books;
    # cursor.execute(f'insert into books values("{name}", "", 0); DROP TABLE books;", 0)')
    
    conn.commit()
    conn.close()


def _save_all_books(books):
    with open(FILE_NAME, 'w') as file:
        json.dump(books, file, indent=4)


def get_all_books():
    conn = sqlite3.connect(FILE_NAME)
    cursor = conn.cursor()
    
    sql = "SELECT * FROM books;"
    cursor.execute(sql)
    
    # books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    books = cursor.fetchall() # [(name, author, read), (name, author, read), ...]
    
    for name, author, read in books:
        read_status = 'YES' if read else 'NO'
        print(f"{name} by {author}, read: {read_status!r}")
    
    conn.close()


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

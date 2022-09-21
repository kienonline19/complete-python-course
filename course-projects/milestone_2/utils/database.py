"""
Concerned with storing and retrieving books from a sqlite database.
"""
import sqlite3
from typing import List, Dict, Union
from .database_connection import DatabaseConnection
HOST = "data.db"

Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    """
    context managers
    with ... as ...:
        pass
    """

    with DatabaseConnection(HOST) as conn:
        cursor = conn.cursor()
        sql_command = """create table if not exists books (
            name text primary key,
            author text,
            read int
        );"""

        cursor.execute(sql_command)


def add_book(name: str, author: str) -> None:
    with DatabaseConnection(HOST) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author))

        # SQL Injection
        # author: ', 0); DROP TABLE books;
        # cursor.execute(f'insert into books values("{name}", "", 0); DROP TABLE books;", 0)')


def get_all_books() -> List[Book]:
    with DatabaseConnection(HOST) as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM books;"
        cursor.execute(sql)

        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        # [(name, author, read), (name, author, read), ...]
        # books = cursor.fetchall()

        # for name, author, read in books:
        #     read_status = 'YES' if read else 'NO'
        #     print(f"{name} by {author}, read: {read_status!r}")

        return books


def mark_book_as_read(book_name: str) -> None:
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE books SET read=1 WHERE name=?", (book_name,))


def delete_book(book_name: str) -> None:
    with DatabaseConnection(HOST) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE name=?", (book_name,))

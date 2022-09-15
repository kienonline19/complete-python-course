import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.conn = None
        self.host = host

    def __enter__(self):
        self.conn = sqlite3.connect(self.host)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

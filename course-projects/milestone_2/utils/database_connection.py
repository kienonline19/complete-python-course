import sqlite3


class DatabaseConnection:
    def __init__(self, host: str):
        self.conn = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.conn = sqlite3.connect(self.host)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if exc_type or exc_val or exc_tb:
        if exc_type is not None or exc_val is not None or exc_tb is not None:
            self.conn.close()
        else:
            self.conn.commit()
            self.conn.close()

import sqlite3

"""
Context Manager.  Define the init method
and entering and exit methods
"""

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_tb or exc_type or exc_value:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

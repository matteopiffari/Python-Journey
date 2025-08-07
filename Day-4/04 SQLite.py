import sqlite3

# Creating a Class Based Context Manager

class Db:
    def __init__(self, path: str):                      # The class constructor
        self.path = path
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.path)    # Setting up the resource
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):      # Closing the external resource
        if exc_type is not None:
            print(f'error: {exc_val}')
        
        self.connection.close()

# Example usage of the Db context manager
# This will create a database file named 'test.db' and a table named 'test'

with Db("test.db") as db:
    db.cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    
    db.cursor.execute('INSERT INTO test (name) VALUES ("John")')
    db.cursor.execute('INSERT INTO test (name) VALUES ("Bob")')

    db.connection.commit()

    db.cursor.execute('SELECT * FROM test')
    print(db.cursor.fetchall())
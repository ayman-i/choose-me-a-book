import sqlite3 as sql

# Initialise an empty database.
def start_db():
    conn = sql.connect("book_database.sqlite")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Book")
    c.execute("CREATE TABLE Book(book_name text)")
    conn.commit()

# Connect to db.
def connect_to_db():  
    conn = sql.connect("book_database.sqlite")
    c = conn.cursor()
    return c, conn

# Add a list of books to db.
def add_to_db(books):
    c, conn = connect_to_db()
    for book in books:
        c.execute("INSERT INTO Book VALUES(?)", (item,))
    conn.commit()

# Get all books from db.
def get_books():
    c, conn = connect_to_db()
    books_left = []
    for row in c.execute("SELECT * FROM Book"):
        books_left.append(row)
    return books_left

# Delete a book from db.
def delete_book(book):
    c, conn = connect_to_db()
    c.execute("DELETE FROM Book WHERE book_name = (?)", (book))
    conn.commit()

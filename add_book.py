from time import sleep as sleep
from initialise_db import sleep_with_message

# Ask the user to enter their book titles, add to database.
def add_books():
    sleep_with_message("Enter the names of the book/s you want to add, separated by commas with a full stop at the end..\n"
                       "i.e. 'Ready Player One, Ready Player Two.'"
                       )
    books = input("Enter: ")

    # Remove leading whitespace, final full stop.
    books_list = books.split(",")
    index = 0
    for book in books_list:
        books_list[index] = book.lstrip()
        index += 1
    books_list[-1] = books_list[-1][:-1]

    add_to_db(books_list)

if __name__ == "__main__":
    add_books()
    sleep_with_message("Books added.")


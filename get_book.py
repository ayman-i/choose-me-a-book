from db_tools import get_books, delete_book
from random import choice as choose_random
import sqlite3
from time import sleep as sleep

books_left = get_books()

# Get a random book and format its name for output to user.
try:
    book_chosen = choose_random(books_left)
    book_chosen_f = str(book_chosen)
    book_chosen_f = book_chosen_f.replace(",", "").replace("'", "").replace("(", "").replace(")", "")
except:
    print("You have read all of the books!")
    sleep(5)
    exit()

# Display to user and remove from database.
print("Your chosen book is...")
sleep(2)
print("{}".format(book_chosen_f))
delete_book(book_chosen)

sleep(10)

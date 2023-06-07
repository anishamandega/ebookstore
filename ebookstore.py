# importing libraries
import sqlite3
from wasabi import Printer

printer = Printer()

# connect to sqlite database
db = sqlite3.connect("ebookstore")

# get a cursor object
cursor = db.cursor()


# Create the "books" table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
""")

# Check if the books are already added by counting the number of rows in the "books" table
cursor.execute("""
SELECT COUNT(*) FROM books
""")
count = cursor.fetchone()[0]

# If the count is greater than zero, the books are already added, so we skip the insertion step
if count == 0:
    # List of tuples containing book data
    values = [
        (3001, "A Tale Of Cities", "Charles Dickens", 30),
        (3002, "Harry Potter And the Philosopher's Stone", "J.K Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S.Lewis", 25),
        (3004, "The Lord Of The Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
    ]

    # Insert multiple rows into the "books" table
    cursor.executemany("""
    INSERT INTO books VALUES (?, ?, ?, ?)
    """, values)

    # Commit the changes to the database
    db.commit()


# defined an add book function
def add_book():
    try:
        # Get the highest existing book ID from the database
        cursor.execute("""
        SELECT MAX(id) FROM books
        """)
        max_id = cursor.fetchone()[0]
        book_id = max_id + 1 if max_id else 3001

        # Ask the user for input on the book they would like to add
        book_title = input("Please enter the title of the book: ")
        book_author = input("Please enter the author of the book: ")
        book_qty = int(input("Please enter the quantity of the book: "))

        # Check if the book already exists in the database
        cursor.execute("""
        SELECT * FROM books WHERE title = ? AND author = ?
        """, (book_title, book_author))

        already_exists = cursor.fetchall()

        # If the book already exists, display a message and return
        if already_exists:
            printer.info("This book already exists in the database.")
            return

        # Insert the book into the "books" table
        cursor.execute("""
        INSERT INTO books VALUES (?, ?, ?, ?)
        """, (book_id, book_title, book_author, book_qty))

        # Commit the changes to the database
        db.commit()

        printer.good("New book added!")

    except ValueError:
        printer.warn("Invalid input, please try again")

    except Exception as e:
        printer.fail("An error occurred while adding the book:", e)


# created an update book function
def update_book():
    while True:

        # printed the menu for the user
        printer.text("              BOOK UPDATE MENU             ", color="pink")
        printer.text("----------------------------------------------------------", color="cyan")
        printer.text("Which of the following options would you like to update:  ")
        printer.text("bt = book title", color="yellow")
        printer.text("ba = book author", color="yellow")
        printer.text("bq = book quantity", color="yellow")
        printer.text("e  = exit", color="yellow")
        printer.text("----------------------------------------------------------", color="cyan")

        # asked user to enter there choice here and used lower to all them to enter there choice in any format
        update_choice = input("Enter here:").lower()

        if update_choice == "bt":

            # used a try except block
            while True:
                try:

                    # asked the user to enter the title of the book they would like to update
                    title_id_update = int(input("Please enter the id of the book you would like to update:"))
                    title_update = input("Please enter the updated title of the book:")

                    # updated book using the book id and updated title entered by the  user
                    cursor.execute("""
                    UPDATE books SET title = ? WHERE id = ?
                    """, (title_update, title_id_update))

                    # selected the updated book by using the title entered by the user
                    cursor.execute("SELECT * FROM books WHERE title = ?", (title_update,))

                    # used fecthone to get the book information
                    new_book = cursor.fetchone()

                    # used an if statement for when the book is found-0
                    if new_book:
                        print("")
                        printer.text(f"BOOK ID           : {new_book[0]}", color="blue")
                        printer.text(f"BOOK TITLE        : {new_book[1]}", color="blue")
                        printer.text(f"BOOK AUTHOR       : {new_book[2]}", color="blue")
                        printer.text(f"BOOK QUANTITY     : {new_book[3]}", color="blue")
                        print("")
                        printer.good("Book updated")

                    # used an else statement for when the book is not found
                    else:
                        printer.fail("Book not found")


                # handles ValueError exceptions
                except ValueError:
                    printer.text("You have entered an invalid input,please try again",  color="red")

        # used elif statement for when user selects to update the book by author
        elif update_choice == "ba":

            # used a try except block
            while True:
                try:

                    # asked the user to enter the id of the book they would like to search
                    id_update = int(input("Please enter the id of the book you would like to update:"))

                    # asked the user to enter the updated name of the author
                    author_update = input("Please enter the updated name of the author:")

                    # updated the book using the book id and updated author entered by the  user
                    cursor.execute("""
                    UPDATE books SET author = ? WHERE id = ?
                    """, (author_update, id_update))

                    # selected the updated book by using the updated author entered by the user
                    cursor.execute("SELECT * FROM books WHERE author = ?", (author_update,))

                    # used fecthone to get the book information
                    new_book = cursor.fetchone()

                    # used an if statement for when the book is found
                    if new_book:
                        print("")
                        printer.text(f"BOOK ID           : {new_book[0]}", color="blue")
                        printer.text(f"BOOK TITLE        : {new_book[1]}", color="blue")
                        printer.text(f"BOOK AUTHOR       : {new_book[2]}", color="blue")
                        printer.text(f"BOOK QUANTITY     : {new_book[3]}", color="blue")
                        print("")
                        printer.good("Book updated")

                    # used an else statement for when the book is not found
                    else:
                        printer.fail("Book not found")

                    # commit to the change
                    db.commit()

                # handles ValueError exceptions
                except ValueError:
                    print("You have entered an invalid input,please try again")

        elif update_choice == "bq":

            # used a try except block
            while True:
                try:
                    # asked the user to enter the id of the book they would like to delete
                    book_id_update = int(input("Please enter the id of the book you would like to update:"))

                    # asked the user to enter the updated quantity of the book
                    book_qty = int(input("Please enter the updated quantity of the book:"))

                    # updated the book using book id and updated quantity entered by the  user
                    cursor.execute("""
                    UPDATE books SET qty = ? WHERE id = ?
                    """, (book_qty, book_id_update))

                    # selected the updated book by using the updated quantity entered by the user
                    cursor.execute("SELECT * FROM books WHERE qty = ?", (book_qty,))

                    # used fecthone to get the book information
                    new_book = cursor.fetchone()

                    # used an if statement for when the book is found
                    if new_book:
                        print("")
                        printer.text(f"BOOK ID        : {new_book[0]}", color="blue")
                        printer.text(f"BOOK TITLE     : {new_book[1]}", color="blue")
                        printer.text(f"BOOK AUTHOR    : {new_book[2]}", color="blue")
                        printer.text(f"BOOK QUANTITY  : {new_book[3]}", color="blue")
                        print("")
                        printer.good("Book updated")
                    # used an else statement for when the book is not found
                    else:
                        printer.fail("\nBook not found")

                    # commit to the change
                    db.commit()

                # handles ValueError exceptions
                except ValueError:
                    printer.warn("You have entered an invalid input,please try again")

        # used elif statement and break for when the user decides to leave the book update menu
        elif update_choice == "e":
            break


# created delete book function
def delete_book():
    while True:

        # printed the menu of options
        printer.text("                  BOOK DELETE MENU               ", color="pink")
        printer.text("-------------------------------------------", color="cyan")
        printer.text("Please select one of the following option:")
        printer.text("dt = delete by title", color="yellow")
        printer.text("da = delete by author", color="yellow")
        printer.text("di = delete by id", color="yellow")
        printer.text("e  = exit", color="yellow")
        printer.text("-------------------------------------------", color="cyan")

        # asked user for input
        delete_choice = input("Enter here: ")

        # used can if statement for when wants to delete by book title
        if delete_choice == "dt":

            # asked the user to input the title of the book they would like to delete
            title_delete = input("Please enter the title of the book like to delete:")

            # deleted the book with book title entered by the  user
            cursor.execute("""
            DELETE FROM books WHERE title = ?
                """, (title_delete,))

            # printed a little message for the user when the book is deleted
            printer.good("Book deleted")

            # commit to the change
            db.commit()

        # used elif for when the user wants to delete by book author
        elif delete_choice == "da":

            # asked the user to enter
            author_delete = input("Please enter the author of the book you would like to delete:")

            # deleted the book with book author entered by the  user
            cursor.execute("""
            DELETE FROM books WHERE author = ?
                """, (author_delete,))

            printer.good("Book deleted")

            # commit to the change
            db.commit()

        elif delete_choice == "di":
            # used a try except block
            while True:
                try:
                    # asked user for the id of the book they would like to delete
                    id_delete = int(input("Please enter the id of the book you would like to delete:"))

                    # deleted the book with book id entered by the  user
                    cursor.execute("""
                        DELETE FROM books WHERE id = ?
                        """, (id_delete,))

                    printer.good("Book deleted")

                    # commit to the change
                    db.commit()
                    break

                # handles ValueError exceptions
                except ValueError:
                    printer.warn("Invalid input, please try again")

        # used an elif statement and break for when the user selects to leave the search menu
        elif delete_choice == "e":
            break


# created a search book function
def search_book():
    while True:

        # printed the search menu
        print("")
        printer.text("                BOOK SEARCH MENU                ", color="pink")
        printer.text("------------------------------------------------", color="cyan")
        printer.text("Please select one of the following options:")
        printer.text("st = search by title", color="yellow")
        printer.text("sa = search by author", color="yellow")
        printer.text("si = search by id", color="yellow")
        printer.text("e  = exit", color="yellow")
        printer.text("-------------------------------------------------", color="cyan")

        # asked the user to input there choice and used lower to allow them to enter the input in any format
        search_choice = input("Enter here: ").lower()

        # used a while to make sure the user enters the proper input

        if search_choice == "st":

            # asked the user to input the title of the book they would like to search
            title_search = input("Please enter the title of the book you would like to search:")

            # selected book with book title entered by the  user
            cursor.execute("""
            SELECT * FROM books WHERE title = ?
            """, (title_search,))

            # used fecthone to get the book information
            books = cursor.fetchone()

            # used an if statement for when the book is found
            if books:
                printer.text("Search results", color="green")
                print("")
                printer.text(f"BOOK ID        : {books[0]}", color="blue")
                printer.text(f"BOOK Title     : {books[1]}", color="blue")
                printer.text(f"BOOK Author    : {books[2]}", color="blue")
                printer.text(f"BOOK Quantity : {books[3]}", color="blue")
                db.commit()

            # used else for when the book is not found
            else:
                printer.text("Book not found.", color="red")

        # use elif statement for when the user selects to search by book author
        elif search_choice == "sa":
            author_search = input("Please enter the author of the book you would like to search:")
            # selected book with book author entered by the  user
            cursor.execute("""
                    SELECT * FROM books WHERE author = ?
                    """, (author_search,))

            # used fecthone to get the book information
            books1 = cursor.fetchall()

            # used an if statement for when the book is found
            if books1:
                print("")
                printer.text("        Search results  ", color="green")
                print("")
                for i, book in enumerate(books1, 1):
                    printer.text(f"BOOK{i}")
                    printer.text(f"BOOK ID       : {book[0]}", color="blue")
                    printer.text(f"BOOK Title    : {book[1]}", color="blue")
                    printer.text(f"BOOK Author   : {book[2]}", color="blue")
                    printer.text(f"BOOK Quantity : {book[3]}", color="blue")
                    print("")
            else:
                printer.text("Book not found.", color="red")
                # commit to the change
                db.commit()

        # used elif statement for when the user selects to search by book id
        elif search_choice == "si":
            while True:
                try:
                    # asked the user to enter the id of the book they would like to enter
                    book_search = int(input("Please enter the id of the book you would like to search:"))

                    # selected book with book id entered by the  user
                    cursor.execute("""
                            SELECT id, title, author, qty FROM books WHERE id = ?
                            """, (book_search,))

                    # used fecthone to get the book information
                    book = cursor.fetchone()

                    # used an if statement for when the book is found
                    if book:
                        print("")
                        printer.text("        Search results  ", color="green")
                        print("")
                        printer.text(f"BOOK ID       : {book[0]}", color="blue")
                        printer.text(f"BOOK Title    : {book[1]}", color="blue")
                        printer.text(f"BOOK Author   : {book[2]}", color="blue")
                        printer.text(f"BOOK Quantity : {book[3]}", color="blue")

                        # commit to the change
                        db.commit()

                    # used an else statement for the book is not found
                    else:
                        printer.text("Book not found.", color="red")

                # handles ValueError exceptions
                except ValueError:
                    printer.warn("Invalid input, please try again")

        # used an elif statement and break for when the user selects to leave the search menu
        elif search_choice == "e":
            break
        else:
            printer.warn("Invalid choice, please try again")
            print("")


def view_all():

    cursor.execute("""
                    SELECT * FROM books 
                    """)

    # used fecthone to get the book information
    books1 = cursor.fetchall()

    # used an if statement for when the book is found
    if books1:
        print("")
        printer.text("        ALL BOOKS  ", color="green")
        print("")
        for i, book in enumerate(books1, 1):
            printer.text(f"BOOK{i}")
            printer.text(f"BOOK ID       : {book[0]}", color="blue")
            printer.text(f"BOOK Title    : {book[1]}", color="blue")
            printer.text(f"BOOK Author   : {book[2]}", color="blue")
            printer.text(f"BOOK Quantity : {book[3]}", color="blue")
            print("")
    else:
        printer.text("Error no books found.", color="red")
        # commit to the change
        db.commit()


while True:

    # printed the book menu
    print("")
    printer.text("                BOOK MANAGEMENT MENU        ", color='pink')
    printer.text("----------------------------------------------------------", color='cyan')
    printer.text("Please select one of the following options:")
    printer.text("ab = Add book", color='yellow')
    printer.text("ub = Update book", color='yellow')
    printer.text("db = Delete book", color='yellow')
    printer.text("sb = Search books", color='yellow')
    printer.text("va = View all books", color='yellow')
    printer.text("e  = Exit", color='yellow')
    printer.text("----------------------------------------------------------", color='cyan')
    user_choice = input('Enter here:').lower()
    print("")

    # used an if statement for when the user selects to add a new book
    if user_choice == "ab":
        print("\nWelcome!\n")
        print("You have selected to add a book\n")

        # called the enter function
        add_book()

    # used elif statement for when user selects to update the book
    elif user_choice == "ub":
        print("\nWelcome!")
        print("You have selected to update a book")

        # called the update book function
        update_book()

    # used elif statement for user selects to delete book
    elif user_choice == "db":
        print("\nWelcome!")
        print("You have selected to delete a book")

        # called to delete book function
        delete_book()

    # used elif statement for when user selects to search book
    elif user_choice == "sb":
        print("\nWelcome!")
        print("You have selected to search for a book")

        # called the search book function
        search_book()

    elif user_choice == "va":
        print("\nWelcome!")
        print("You have selected to view all books")
        view_all()

    # used an elif statement for when the user selects to exit the menu
    elif user_choice == "e":
        printer.text("You have selected to exit the Book Management Menu", color="cyan")
        printer.text("Goodbye!!!", color="cyan")
        # exited the code
        exit()
        db.close()

    else:
        printer.warn("Invalid choice, please try again")

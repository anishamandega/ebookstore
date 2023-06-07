# Ebootstore
This is a simple ebookstore that makes use of python and sqlite to store books in a database. The program allows you to add, delete, search, update and view all books in the ebookstore database.

# Requirements
To run the EbookStore application, you need to have the following software installed on your system:

Python 3.x
SQLite
Wasabi

# Getting Started

1. Clone the repository or download the source code files to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

# Installation

1. Install the required Python libraries by running the following command:
$ pip install -r requirements.txt

# Usage

Run the program by executing the following command:
$ python ebookstore.py

The program will start and display a menu with different options to manage the eBook store.

# Features 
The eBook store management system provides the following features:

Add a Book: Allows the user to add a new book to the store. The user is prompted to enter the title, author, and quantity of the book.

Update a Book: Allows the user to update the information of an existing book in the store. The user can choose to update the book title, author, or quantity.

Delete a Book: Allows the user to delete a book from the store. The user can choose to delete a book by its title, author, or ID.

Search for a Book: Allows the user to search for a book in the store. The user can search for a book by its title, author, or ID.

# Database
The program uses an SQLite database to store the book information. The database is named "ebookstore.db" and is automatically created when the program runs for the first time.

The "books" table in the database has the following columns:

id (INTEGER): Unique identifier for each book.
title (TEXT): Title of the book.
author (TEXT): Author of the book.
qty (INTEGER): Quantity of the book available in the store.

# Contributing
Contributions to this project are welcome. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

# Acknowledgments
This project is based on a programming exercise I completed during the bootcamp at HyperionDev.
The Wasabi library is used for colorful console output.


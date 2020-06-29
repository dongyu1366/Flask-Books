# Project 1
This project builds a book review website. You can use ISBN, book title or author to search books, and see detail about a book(ISBN, title, author, year, reviews, rating). You also can register and login to write a review for a book. The website also provides API to let people get the data of each book.

## Project structure
- application.py: contain main code, include all view functions
- tables.py: define and create three tables into the database
- import.py: import data from book.csv into database
- config.py: configure API_key to use Goodreads API
- static floder: contains all static files
- templates floder: contains all html files

## How to run
1. Create a virtual environment and install requirements
$ pip install -r requirements.txt
2. Set environment variables
$ export FLASK_APP=application.py
$ export FLASK_DEBUG=1
$ export DATABASE_URL="{Your database_url}"
3. Create table and import data into database
$ python tables.py
$ python import.py
4. In config.py, set your API_key, it use my key by default
5. Run the app
$ flask run

## API Access
Make a GET request to your website’s /api/{isbn} route, where {isbn} is an ISBN number, your website would return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score.

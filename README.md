# Flask-Library
This project is developed by **Flask** and **PostgreSQL**, it builds a book review website. You can use ISBN, book title or author to search books, and see detail about a book(ISBN, title, author, year, reviews, rating). You also can register and login to write a review for a book. The website also provides API to let people get the data of each book.

Video demo : https://youtu.be/JBpZfvOW8l4   
Heroku: https://dong-project01-book.herokuapp.com/    

## All Functions
- **Registration, login and logout**
- **Search:** Users are able to type in the ISBN number of a book, the title of a book, or the author of a book to search.
- **Review Submission:** Users can submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. 
- **Goodreads Review Data:** External API is used. On any book page , it would display(if available) the average rating and number of ratings the work has received from [Goodreads](https://www.goodreads.com/api).
-** API Access: **Make a GET request to your website's `/api/<isbn>` route, where `<isbn>` is an ISBN number, your website would return a JSON response containing the book's title, author, publication date, ISBN number, review count, and average score.

## Project structure
- **application.py:** Contain main code, include all view functions
- **tables.py:** Define and create three tables into the database
- **import.py:** Import data from book.csv into database
- **config.py:** Configure API_key to use Goodreads API and database url
- **static directory:** Contains all static files
- **templates directory:** Contains all html files

## How to use

1. Create a virtual environment and install requirements
$ pip install -r requirements.txt      
2. Configure config.py   
API_key & DATABASE_URL
3. Create table and import data into database
$ python tables.py
$ python import.py
4. Run the app
$ python application.py

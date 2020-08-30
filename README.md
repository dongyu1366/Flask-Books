# Flask-Library
#### Technicle: flask, docker
This project is developed by **Flask**, it builds a book review website. You can use ISBN, book title or author to search books, and see detail about a book(ISBN, title, author, year, reviews, rating). You also can register and login to write a review for a book. The website also provides API to let people get the data of each book.

Video demo : https://youtu.be/JBpZfvOW8l4   
Heroku: https://dongyu-dcoker-library.herokuapp.com    


## All Functionalities
- **Registration, login and logout**
- **Search:** Users are able to type in the ISBN number of a book, the title of a book, or the author of a book to search.
- **Review Submission:** Users can submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book.    
- **Goodreads Review Data:** External API is used. On any book page , it would display(if available) the average rating and number of ratings the work has received from [Goodreads](https://www.goodreads.com/api).   
- **API Access:** Make a GET request to your website's `/api/<isbn>` route, where `<isbn>` is an ISBN number, your website would return a JSON response containing the book's title, author, publication date, ISBN number, review count, and average score.


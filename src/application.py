import os
import requests
import decimal
import flask.json

from flask import Flask, flash, session, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
from config import API_key
#
app = Flask(__name__)
app.secret_key = 'dsfasdfqr32543trehgedfgsd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from core.controller import *
from orm.models import *
#
# # Check for environment variable
# if not DATABASE_URL:
#     raise RuntimeError("DATABASE_URL is not set")
#
# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
#
# Set up database
# engine = create_engine(DATABASE_URL)
# db = scoped_session(sessionmaker(bind=engine))
#
# # Override the application's JSON encoder
#
#
# class MyJSONEncoder(flask.json.JSONEncoder):
#
#     def default(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             # Convert decimal instances to float.
#             return float(obj)
#         return super(MyJSONEncoder, self).default(obj)
#
#
# app.json_encoder = MyJSONEncoder
#
#
# @app.route("/")
# def index():
#
#     return render_template("index.html")
#
#
# @app.route("/register", methods=["GET", "POST"])
# def register():
#
#     # check user is already login or not
#     if session.get("username"):
#         username = session["username"]
#         flash(f"Welcome, {username}!", "success")
#         return render_template("index.html")
#
#     # Get the information of registrition and insert to database
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         password2 = request.form.get("password2")
#
#         # Make sure the username has not been used
#         if db.execute("SELECT username FROM users WHERE username=:username", {"username": username}).rowcount != 0:
#             flash("Username aldready exists.", "warning")
#             return render_template("register.html")
#
#         # Make sure confirm password is same as password
#         if password != password2:
#             flash("Passwords are inconsistent.", 'warning')
#             return render_template("register.html")
#
#         # Store username & password into database then login
#         try:
#             db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
#                        {"username": username, "password": password})
#             db.commit()
#             session["username"] = username
#             flash(f"{username}, your account has been created!", "success")
#             return redirect(url_for('index'))
#         except:
#             flash("Something wrong, please try another username.", "warning")
#             return render_template("register.html")
#
#     return render_template("register.html")
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#
#     # check user is already login or not
#     if session.get("username"):
#         username = session["username"]
#         flash(f"Welcome, {username}!", "success")
#         return render_template("index.html")
#
#     # check the input username & password are valid or not
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         try:
#             user = db.execute("SELECT * FROM users WHERE username=:username AND password=:password",
#                               {"username": username, "password": password}).fetchone()
#             session["username"] = user.username
#             flash(f"{username}, welcome be back!", "success")
#             return redirect(url_for('index'))
#         except:
#             flash("Invalid username or password. Please try again.", 'danger')
#             return redirect(url_for('login'))
#
#     return render_template("login.html")
#
#
# @app.route("/logout")
# def logout():
#
#     # reset data of session
#     session.clear()
#
#     return redirect(url_for('login'))
#
#
# @app.route("/search", methods=["GET", "POST"])
# def search():
#
#     # Get what user input and search
#     if request.method == "POST":
#         isbn = request.form.get("isbn")
#         title = request.form.get("title")
#         author = request.form.get("author")
#
#         # Make sure user has input some key word for search
#         if isbn == title == author == '':
#             return render_template("search.html")
#
#         # Searching from database
#         try:
#             books = db.execute("SELECT * FROM books WHERE isbn LIKE :isbn AND LOWER(title) LIKE LOWER(:title) AND "
#                                "LOWER(author) LIKE LOWER(:author)",
#                                {"isbn": f"%{isbn}%", "title": f"%{title}%", "author": f"%{author}%"}).fetchall()
#             if books:
#                 return render_template("search.html", books=books)
#             else:
#                 flash("No matches, please try another key words.", "warning")
#                 return render_template("search.html")
#         except:
#             flash("Oops! Please try again.", "warning")
#             return render_template("search.html")
#
#     return render_template("search.html")
#
#
# @app.route("/detail/<int:book_id>", methods=["GET", "POST"])
# def detail(book_id):
#
#     # Make sure the book exists.
#     book = db.execute("SELECT * FROM books WHERE id=:id",
#                       {"id": book_id}).fetchone()
#     if book is None:
#         flash("Sorry, no such book.", "warning")
#         return redirect(url_for('search'))
#
#     # Get the rating form Goodreads if available
#     isbn = book.isbn
#     res = requests.get("https://www.goodreads.com/book/review_counts.json",
#                        params={"key": API_key, "isbns": f"{isbn}"})
#     try:
#         res = res.json()
#         average_rating = res["books"][0]["average_rating"]
#         work_ratings_count = res["books"][0]["work_ratings_count"]
#         goodreads = {"average_rating": average_rating,
#                      "work_ratings_count": work_ratings_count}
#     except:
#         goodreads = {"average_rating": "None", "work_ratings_count": "None"}
#
#     # Get all reviews from database
#     reviews = db.execute("SELECT * FROM reviews WHERE book_id=:id",
#                          {"id": book_id}).fetchall()
#
#     # Make a review and store into database, one user can only make one review for the same book
#     if request.method == "POST":
#         if session.get("username"):
#             username = session["username"]
#             rating = int(request.form.get("rating"))
#             content = request.form.get("content")
#
#             # Make sure the user have not leaved a review
#             if db.execute("SELECT username FROM reviews WHERE username=:username AND book_id=:book_id",
#                           {"username": username, "book_id": book_id}).rowcount != 0:
#                 flash("You have already make a review.", "warning")
#                 return redirect(url_for('detail', book_id=book.id))
#
#             # Save the review into database
#             try:
#                 db.execute("INSERT INTO reviews (book_id, rating, content, username) \
#                             VALUES (:book_id, :rating, :content, :username)",
#                            {"book_id": book_id, "rating": rating, "content": content, "username": username})
#                 db.commit()
#                 flash("Success", "success")
#                 return redirect(url_for('detail', book_id=book.id))
#             except:
#                 flash("Oops! Please try again.", "warning")
#                 return redirect(url_for('detail', book_id=book.id))
#         else:
#             flash("You have to login first.", "warning")
#             return redirect(url_for('login'))
#
#     return render_template("detail.html", book=book, reviews=reviews, goodreads=goodreads)
#
#
# @app.route("/api/<string:isbn>")
# def books_api(isbn):
#     """
#     Return details about a single book.
#     """
#
#     # Selecting the book from database
#     book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
#
#     # Make sure the book exists.
#     if book is None:
#         return jsonify({"error": "Invalid isbn"}), 404
#
#     # Get needed details about the book
#     review_count = db.execute("SELECT COUNT(*) FROM reviews JOIN books ON books.id = reviews.book_id \
#                                WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
#     average_score = db.execute("SELECT AVG(rating) FROM reviews JOIN books ON books.id = reviews.book_id \
#                                WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
#     data = {
#         "title": book.title,
#         "author": book.author,
#         "year": book.year,
#         "isbn": book.isbn,
#         "review_count": review_count.count,
#         "average_score": average_score.avg
#     }
#
#     return jsonify(data)





if __name__ == '__main__':
    db.create_all()
    app.run()


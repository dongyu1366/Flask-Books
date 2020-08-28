from application import app
from flask import flash, session, render_template, request, redirect, url_for
from handler.user_handler import UserHandler, UserDatabase
from handler.book_handler import BookHandler
from handler.review_handler import ReviewHandler


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def user_register():
    # check user is already login or not
    if UserHandler.check_login_status():
        username = session["username"]
        flash(f"Welcome, {username}!", "success")
        return render_template("index.html")

    # Get the information of registrition and insert to database
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # Make sure the username has not been used
        if UserDatabase.check_username_exist(username):
            flash("Username has already been used.", "warning")
            return render_template("register.html")

        # Make sure confirm password is same as password
        if UserHandler.confirm_password(password, password2):
            flash("Inconsistent passwords.", 'warning')
            return render_template("register.html")

        # Store username & password into database then login
        try:
            UserDatabase.insert_user_to_db(username=username, password=password)
            session["username"] = username
            flash(f"{username}, your account has been created!", "success")
            return redirect(url_for('index'))
        except:
            flash("Something wrong, please try another username.", "warning")
            return render_template("register.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def user_login():
    # check user is already login or not
    if UserHandler.check_login_status():
        username = session["username"]
        flash(f"Welcome, {username}!", "success")
        return render_template("index.html")

    # check the input username & password are valid or not
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if UserHandler.validate_login(username=username, password=password):
            username = UserHandler.validate_login(username=username, password=password)
            flash(f"{username}, welcome be back!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password. Please try again.", 'danger')
            return redirect(url_for('user_login'))
    return render_template("login.html")


@app.route("/logout")
def user_logout():
    # reset data of session
    session.clear()
    return redirect(url_for('user_login'))


@app.route("/search", methods=["GET", "POST"])
def books_search():
    # Get what user input and search
    if request.method == "POST":
        isbn = request.form.get("isbn")
        title = request.form.get("title")
        author = request.form.get("author")

        if BookHandler.check_search_empty(isbn=isbn, title=title, author=author):
            return render_template("search.html")
        else:
            books = BookHandler.search_books(isbn=isbn, title=title, author=author)
            if books:
                return render_template("search.html", books=books)
            else:
                flash("No matches, please try another key words.", "warning")
                return render_template("search.html")
    return render_template("search.html")


@app.route("/detail/<int:book_id>", methods=["GET", "POST"])
def book_detail(book_id):
    book = BookHandler.get_the_book(book_id=book_id)
    if book is None:
        flash("Sorry, no such book.", "warning")
        return redirect(url_for('search'))

    # Get the rating form Goodreads if available
    isbn = book.isbn
    goodreads_rating = BookHandler.get_goodreads_rating(isbn=isbn)

    # Get all reviews from database
    reviews = ReviewHandler.get_all_review(book_id=book_id)

    # Create a review and insert to database, one user can only make one review for the same book
    if request.method == "POST":
        if session.get("username"):
            username = session["username"]
            rating = int(request.form.get("rating"))
            content = request.form.get("content")

            # Make sure the user has not leave a review before
            if ReviewHandler.check_review_already(username=username, book_id=book_id):
                flash("You have already make a review.", "warning")
                return redirect(url_for('book_detail', book_id=book.id))

            # Insert the review into database
            try:
                ReviewHandler.insert_review_to_db(book_id=book_id, username=username, rating=rating, content=content)
                flash("Success", "success")
                return redirect(url_for('book_detail', book_id=book.id))
            except:
                flash("Oops! Please try again.", "warning")
                return redirect(url_for('book_detail', book_id=book.id))
        else:
            flash("You have to login first.", "warning")
            return redirect(url_for('user_login'))
    return render_template("detail.html", book=book, reviews=reviews, goodreads=goodreads_rating)

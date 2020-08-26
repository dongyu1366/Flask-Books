import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# connect to the database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# create table of users
def users_table():
    db.execute("""CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR NOT NULL UNIQUE,
        password VARCHAR NOT NULL
    )
    """)
    db.commit()

# create table of books
def books_table():
    db.execute("""CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        isbn VARCHAR NOT NULL UNIQUE,
        title VARCHAR NOT NULL,
        author VARCHAR NOT NULL,
        year INTEGER NOT NULL
    )
    """)
    db.commit()

# create table of reviews
def reviews_table():
    db.execute("""CREATE TABLE IF NOT EXISTS reviews (
        id SERIAL PRIMARY KEY,
        book_id INTEGER REFERENCES books,
        rating INTEGER NOT NULL,
        content VARCHAR NOT NULL,
        username VARCHAR NOT NULL,
        UNIQUE (book_id, username)
    )
    """)
    db.commit()

if __name__ == "__main__":
    users_table()
    books_table()
    reviews_table()

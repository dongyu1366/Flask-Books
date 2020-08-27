import requests
from flask import Flask, flash, session, render_template, request, redirect, url_for, jsonify
from sqlalchemy import func
from application import db
from orm.models import Book


class BookHandler:
    @classmethod
    def check_search_empty(cls, isbn,  title, author):
        """
        Make sure user has input some key word for searching
        """
        if isbn == title == author == '':
            print('empty')
            return True

    @classmethod
    def search_books(cls, isbn, title, author):
        args = []
        if isbn:
            args.append(Book.isbn.like(f'%{isbn}%'))
        if title:
            title = title.lower()
            args.append(func.lower(Book.title).like(f'%{title}%'))
        if author:
            author = author.lower()
            args.append(func.lower(Book.author).like(f'%{author}%'))

        books = Book.query.filter(*args).all()
        return books

    @classmethod
    def get_the_book(cls, book_id):
        book = Book.query.filter_by(id=book_id).first()
        return book

    @classmethod
    def get_goodreads_rating(cls, isbn):
        response = requests.get("https://www.goodreads.com/book/review_counts.json",
                                params={"key": 'Q0kQoBRDnr3b2b501C7jiQ', "isbns": f"{isbn}"})
        try:
            response = response.json()
            average_rating = response["books"][0]["average_rating"]
            work_ratings_count = response["books"][0]["work_ratings_count"]
            goodreads = {"average_rating": average_rating,
                         "work_ratings_count": work_ratings_count}
            return goodreads
        except:
            goodreads = {"average_rating": "None", "work_ratings_count": "None"}
            return goodreads

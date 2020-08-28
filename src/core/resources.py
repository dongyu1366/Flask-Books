from flask_restful import Resource, fields, marshal
from sqlalchemy import func
from application import db
from orm.models import Book, Review

BookApi_field = {
    'title': fields.String,
    'author': fields.String,
    'year': fields.Integer,
    'isbn': fields.String,
    'review_count': fields.Integer,
    'average_rating': fields.Float,
}


class BookApi(Resource):
    """
    Return details about a single book.
    """
    def get(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if not book:
            return {'error': 'Invalid ISBN'}, 404

        review_count = Review.query.filter_by(book_id=book.id).count()
        average_rating = db.session.query(func.avg(Review.rating)).filter_by(book_id=book.id).scalar()
        data = {'title': book.title,
                'author': book.author,
                'year': book.year,
                'isbn': book.isbn,
                'review_count': review_count,
                'average_rating': average_rating}
        return marshal(data, BookApi_field)

from flask_restful import Resource, fields, marshal
from orm.models import Book

BookApi_field = {
    'title': fields.String,
    'author': fields.String,
    'year': fields.Integer,
}


class BookApi(Resource):
    """
    Return details about a single book.
    """
    def get(self, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if not book:
            return {'error': 'Invalid ISBN'}, 404
        data = {'title': book.title,
                'author': book.author,
                'year': book.year}
        return marshal(data, BookApi_field)

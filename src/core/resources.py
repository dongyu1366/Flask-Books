from flask_restful import Resource, Api
from orm.models import Book


class Books(Resource):
    def get_books(self):
        pass

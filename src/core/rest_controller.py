from flask_restful import Api
from app import app
from core.resources import BookApi


api = Api(app)
api.add_resource(BookApi, '/api/<string:isbn>')


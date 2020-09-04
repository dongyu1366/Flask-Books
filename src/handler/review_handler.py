from app import db
from orm.models import Review


class ReviewHandler:
    @classmethod
    def get_all_review(cls, book_id):
        reviews = Review.query.filter_by(book_id=book_id).all()
        return reviews

    @classmethod
    def check_review_already(cls, username, book_id):
        review = Review.query.filter_by(username=username, book_id=book_id).first()
        return review

    @classmethod
    def insert_review_to_db(cls, book_id, username, rating, content):
        review = Review(book_id=book_id, username=username, rating=rating, content=content)
        db.session.add(review)
        db.session.commit()

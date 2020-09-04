from flask import session
from app import db
from orm.models import User


class UserHandler:
    @classmethod
    def check_login_status(cls):
        """
        check user is already login or not
        """
        if session.get("username"):
            return True

    @classmethod
    def confirm_password(cls, password, password2):
        if password != password2:
            return True

    @classmethod
    def validate_login(cls, username, password):
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session["username"] = user.username
            username = user.username
            return username


class UserDatabase:
    @classmethod
    def check_username_exist(cls, username):
        """
        check the username is exist or not
        """
        if User.query.filter_by(username=username).first():
            return True

    @classmethod
    def insert_user_to_db(cls, username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

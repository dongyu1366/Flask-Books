import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import books


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
app.secret_key = 'dsfasdfqr32543trehgedfgsd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from core.controller import *
from core.rest_controller import *
from orm.models import *

if __name__ == '__main__':
    db.create_all()
    books.insert_csv_to_db()
    app.run(debug=True, host='0.0.0.0', port=port)

import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)

app.secret_key = 'qrfasdga749thgejfkdbnnoqwLDK'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@mysql-server:3306/library"

db = SQLAlchemy(app)
db.init_app(app)

port = int(os.environ.get("PORT", 5000))

from core.controller import *
from core.rest_controller import *
from orm.models import *


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)

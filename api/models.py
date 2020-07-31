from datetime import datetime
from api import db

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0)
    date_created = db.Column(db.DateTime, default=datetime.now)
    last_modified = db.Column(db.DateTime, default=datetime.now)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)


# These are the actual representation of the Book and User data in the database

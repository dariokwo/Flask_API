from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the flask APP and setup database configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = ""
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

# Using SQLALCHEMY to manage database
db = SQLAlchemy(app)

from api import routes
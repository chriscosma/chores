from flask import Flask
from os import urandom
from datetime import datetime
from pytz import timezone
from flask_sqlalchemy import SQLAlchemy

ENGINE_URI = "sqlite:///chores.db"

app = Flask(__name__)
app.secret_key = urandom(12).hex()
app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE_URI

db: SQLAlchemy = SQLAlchemy(app)
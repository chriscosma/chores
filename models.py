from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import calendar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db: SQLAlchemy = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "people"
    name = db.Column(db.String, primary_key=True)
    phone_number = db.Column(db.String(12))
    task = db.Column(db.)
    task = db.relationship('Task', back_populates="people")

class Task(db.Model):
    __tablename__ = "tasks"
    type =  db.Column(db.String, primary_key=True)
    base_points = db.Column(db.Integer)

class TaskHistory(db.Model):
    __tablename__ = "task_history"
    person = db.relationship('Person', back_populates="task_history")
    task = db.relationship('Task', back_populates="task_history")
    date_assigned = db.Column(db.DateTime, nullable=False,
        default=datetime.now(timezone('EST')))
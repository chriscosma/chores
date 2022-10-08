from datetime import datetime
from pytz import timezone
from app import db

class Task(db.Model):
    __tablename__ = "tasks"
    type =  db.Column(db.String, primary_key=True)
    base_points = db.Column(db.Integer)

class Person(db.Model):
    __tablename__ = "people"
    name = db.Column(db.String, primary_key=True)
    phone_number = db.Column(db.String(12))
    task = db.Column(db.ForeignKey(Task.type), nullable=True)

class TaskHistory(db.Model):
    __tablename__ = "task_history"
    person = db.Column(db.ForeignKey(Person.name), primary_key=True)
    task = db.Column(db.ForeignKey(Task.type), primary_key=True)
    date_assigned = db.Column(db.DateTime, nullable=False,
        default=datetime.now(timezone('EST')))
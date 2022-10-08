from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import calendar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
class Person(db.Model):
    name = db.Column(db.String, primary_key = True)
    gbpoints = db.Column(db.Integer)
    number = db.Column(db.String(12))
    task_id = db.Column(db.Integer, db.ForiegnKey('task.id'))
    task = db.relationship('Task',backref=db.backref('person', lazy=True))

class Task(db.Model):
    base_points = db.Column(db.Integer)
    type =  db.Column(db.String)
    id =  db.Column(db.Integer, primary_key = True)
    date_assigned = db.Column(db.DateTime, nullable=False,
        default=datetime.now(timezone('EST')))

class Month(db.Model):
    today = datetime.date.today()
    start = db.Column(db.DateTime, nullable=False,
        default=today)
    end = db.Column(db.DateTime, nullable=False, 
        defalut =datetime.date(today.year, today.month, calendar.monthrange(today.year, today.month)[1]))
    gbotm = db.Column(db.String)
    

class History(db.Model):
    person = db.relationship('Person', backref=db.backref('person', lazy=True))
    task = db.relationship('Task', backref=db.backref('task', lazy=True))
    month = db.relationship('Month', backref=db.backref('month', lazy=True))
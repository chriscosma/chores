import datetime
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
    person = db.Column(db.String, db.ForeignKey(Person.name), primary_key=True)
    task = db.Column(db.String, db.ForeignKey(Task.type), primary_key=True)
    date_assigned = db.Column(db.DateTime, nullable=False,
        default=datetime.date.today())
    #date_completed = db.Column(db.DateTime, nullable=False)
    
    @classmethod
    def get_gbp(cls, person_name: str):
        gbp = 0
        history = cls.query.filter_by(person=person_name)
        for row in history:
            if row.date_assigned.month == datetime.date.today().month:
                task = Task.query.filter_by(type=row.task).first()
                num_days = (datetime.date.today() - row.date_assigned.date).days
                pts = task.base_points - (task.base_points / 14) * num_days
                pts = int(max(pts, task.base_points / 14))
                gbp += pts
        
        return gbp
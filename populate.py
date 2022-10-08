from app import db, app
from models import Person, Task, TaskHistory

people = [
    {
        'name': 'Chris',
        'phone_number': '+14402129348'
    },
    {
        'name': 'Ethan',
        'phone_number': '+14407992892'
    },
    {
        'name': 'Cole',
        'phone_number': '+16146234052'
    },
    {
        'name': 'Ian',
        'phone_number': '+16147720362'
    },
    {
        'name': 'Riley',
        'phone_number': '+12162009570'
    },
    {
        'name': 'Gus',
        'phone_number': '+14407990566'
    },
    {
        'name': 'Alex',
        'phone_number': '+14408405556'
    },
    {
        'name': 'Will',
        'phone_number': '+14192772211'
    },
]

tasks = [
    {
        'type': 'Clean the kitchen',
        'base_points': 14 * 20
    },
    {
        'type': 'Clean bathroom',
        'base_points': 14 * 25
    },
    {
        'type': 'Clean and vaccuum living room',
        'base_points': 14 * 10
    },
    {
        'type': 'Vaccuum stairs and hallway',
        'base_points': 14 * 10
    },
    {
        'type': '(Un)load the dishwasher',
        'base_points': 50
    }
]

task_history = []

copy = tasks.copy()
copy.shuffle()
for person in people:
    task_history.append({
        'person': person['name'],
        'task': copy.pop()
    })

def populate(db):
    for person in people:
        person = Person(**person)
        db.session.add(person)

    for task in tasks:
        task = Task(**task)
        db.session.add(task)
    
    for history in task_history:
        history = TaskHistory(**history)
        db.session.add(history)

    db.session.commit()

with app.app_context():
    db.create_all()
    populate(db)
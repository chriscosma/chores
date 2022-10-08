from models import Person, Task
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database
import logging

ENGINE_URI = "sqlite:///chores.db"

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

def populate(engine):
    with Session(engine) as s:
        for person in people:
            person = Person(**person)
            s.add(person)

        for task in tasks:
            task = Task(**task)
            s.add(task)

        s.commit()

engine = create_engine(ENGINE_URI)
if not database_exists(engine.url):
    logging.info('Database does not exist, creating new one')
    create_database(engine.url)
    populate(engine)


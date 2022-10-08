from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
from app import app, db
from flask import request, render_template, flash
from models import TaskHistory,Person

load_dotenv()

account_sid = "AC098088406eba83d10b50adafa255a22c"
auth_token  = os.environ["AUTH_TOKEN"]

client = Client(account_sid, auth_token)

@app.route("/sms", methods=['GET', 'POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    print("Incoming webhook request")
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def index():
    people = get_people_chores()
    if request.method == 'POST':
        person = request.form['person']
        with app.app_context():
            TaskHistory.mark_task_completed(person)
        flash('Thanks for doing your chore, {}!'.format(person))
    
    return render_template("index.html", people=people, gbotm=", ".join(get_gbotm(people)))

def get_people_chores(sort=False):
    people = []
    with app.app_context():
        rows = Person.query.all()
        for row in rows:
            people.append({
                'name': row.name,
                'gb_points': TaskHistory.get_gbp(row.name),
                'chore': row.task,
                'completed': TaskHistory.is_task_done(row.name)
                })

    if sort:
        people.sort(reverse=True, key=lambda person: person['gb_points'])
    
    return people

def get_gbotm(people):
    points = [person['gb_points'] for person in people]
    max_score = max(points)
    good_boys = [person['name'] for person in people if person['gb_points'] == max_score]
    return good_boys


app.run(debug=True, port=5006)
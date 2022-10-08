from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, redirect

load_dotenv()

account_sid = "AC098088406eba83d10b50adafa255a22c"
auth_token  = os.environ["AUTH_TOKEN"]

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    print("Incoming webhook request")
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

@app.route("/")
def index():
    return render_template("index.html", people=get_people_chores())

def get_people_chores(sort=False):
    people = [
        {
            'name': 'Chris',
            'gb_points': 100,
            'chore': 'Clean kitchen'
        },
        {
            'name': 'Riley',
            'gb_points': 101,
            'chore': 'Clean bathroom'
        }
    ]

    if sort:
        people.sort(reverse=True, key=lambda person: person['gb_points'])
    
    return people

@app.route("/mark_chore_done", methods=['POST'])
def mark_chore_done():
    person = request.form['person']
    # Do something with person name
    return redirect('/')

app.run(debug=True, port=5005)
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
from flask import Flask, request, redirect, send_file

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
    return send_file("index.html")

app.run(debug=True, port=5005)
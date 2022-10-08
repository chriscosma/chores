from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC098088406eba83d10b50adafa255a22c"
# Your Auth Token from twilio.com/console
auth_token  = "db6fea34de15556660c79f63638c655a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14402129348", 
    from_="+19259405257",
    body="Hello from Python!")

print(message.sid)
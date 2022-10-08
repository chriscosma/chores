from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC098088406eba83d10b50adafa255a22c"
# Your Auth Token from twilio.com/console
auth_token  = "0cfc8fd29e64d3a80ab8ee108d1ef590"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14402129348", 
    from_="+19259405257",
    body="Hello from Python!")

print(message.sid)
from twilio.rest import Client

account_sid = "AC402209314e562295bd"
auth_token = "c130f7c2099ed12"
client = Client(account_sid, auth_token)

call = client.messages.create(body="Ba7ebk <3",  to="+201289982884",  from_="+17196314223")

print(call.sid)
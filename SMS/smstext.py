# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf24c5cf6356eb55dccb840e5dc9ae7f9'
auth_token = '51e19c5061c631a1181f5e78ad220bd6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey there! I am sending a SMS through python. --tiku",
                     from_='+18317774550',
                     to='+917359459730'
                 )

print(message.sid)
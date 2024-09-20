from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass

from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=f'whatsapp:{os.getenv("TWILIO_FROM")}',
  body='Your appointment is coming up on July 21 at 3PM',
  to=f'whatsapp:{os.getenv("TWILIO_TO")}'
)

print(message.sid)
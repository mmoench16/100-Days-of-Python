from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

class NotificationManager:
  #This class is responsible for sending notifications with the deal flight details.
  def __init__(self):
      self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
      self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
      self.client = Client(self.account_sid, self.auth_token)
  
  def send_whatsapp_message(self, message):
    message = self.client.messages.create(
      from_=f'whatsapp:{os.getenv("TWILIO_FROM")}',
      body=message,
      to=f'whatsapp:{os.getenv("TWILIO_TO")}'
    )
    print(message)
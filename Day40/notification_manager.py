import os
import smtplib
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.from_email = os.environ["MY_EMAIL"]
        self.app_password = os.environ["APP_PASSWORD"]

    # def send_sms(self, message_body):
    #     """
    #     Sends an SMS message through the Twilio API.
    #     This function takes a message body as input and uses the Twilio API to send an SMS from
    #     a predefined virtual number (provided by Twilio) to your own "verified" number.
    #     It logs the unique SID (Session ID) of the message, which can be used to
    #     verify that the message was sent successfully.

    #     Parameters:
    #     message_body (str): The text content of the SMS message to be sent.

    #     Returns:
    #     None

    #     Notes:
    #     - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
    #     your environment (.env file) and correspond with numbers registered and verified in your
    #     Twilio account.
    #     - The Twilio client (`self.client`) should be initialized and authenticated with your
    #     Twilio account credentials prior to using this function when the Notification Manager gets
    #     initialized.
    #     """
    #     message = self.client.messages.create(
    #         from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
    #         body=message_body,
    #         to=os.environ["TWILIO_VIRTUAL_NUMBER"]
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_FROM"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_TO"]}'
        )
        print(message.sid)

    def send_emails(self, recipient_email, message_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.app_password)
            connection.sendmail(from_addr=self.from_email, 
                                to_addrs=recipient_email, 
                                msg=message_body)
            print(f"Sending email to {recipient_email}..."
                  f" with message: {message_body}")

import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

with open("quotes.txt") as file:
    quotes = file.readlines()

now = dt.datetime.now()

def send_quote(quote):
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("APP_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="", 
                            msg=f"Subject:Motivational Quote\n\n{quote}")

if now.weekday() == 3:
    quote = random.choice(quotes)
    send_quote(quote)

# import smtplib
# import os
# from dotenv import load_dotenv

# load_dotenv()

# my_email = os.getenv("MY_EMAIL")
# password = os.getenv("APP_PASSWORD")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="m.moench16@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)
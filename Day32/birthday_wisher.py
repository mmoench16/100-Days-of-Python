##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random
import pandas

# Load .env file
load_dotenv()

# Load birthdays & transform into dict
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = { (row.month, row.day):row for (_, row) in birthdays.iterrows()}

# Read all letter templates
letter_templates = []
for file in os.listdir("letter_templates"):
    if file.endswith(".txt"):
        with open(f"letter_templates/{file}") as template:
            letter_templates.append(template.read())

now = dt.datetime.now()

def send_quote(message, recipient_email):
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("APP_PASSWORD")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recipient_email, 
                            msg=message)

if (now.month, now.day) in birthdays_dict:
    letter_template = random.choice(letter_templates)
    letter_template = letter_template.replace("[NAME]", birthdays_dict.get((now.month, now.day))['name'])
    letter_template = "Subject:Happy Birthday\n\n" + letter_template
    send_quote(message=letter_template, recipient_email=birthdays_dict.get((now.month, now.day))['email'])
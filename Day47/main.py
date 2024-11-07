from bs4 import BeautifulSoup
import requests
from pprint import pprint
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Amazon
practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = ""


response = requests.get(url=practice_url)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.select_one(selector="span .a-price-symbol").text + soup.select_one(selector="span .a-price-whole").text + soup.select_one(selector="span .a-price-fraction").text
price_without_currency = price[1:]
price_as_float = float(price_without_currency)

print(price_as_float)

# Email

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

from_email = os.environ["MY_EMAIL"]
to_email = os.environ["RECIPIENT_EMAIL"]
app_password = os.environ["APP_PASSWORD"]

BUY_PRICE = 100

if price_as_float < BUY_PRICE:

    message = f"Subject:Amazon Price Alert!\n\nThe price of {title} is now {price_as_float}!\n\nCheck it out here: {practice_url}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email, password=app_password)
                connection.sendmail(from_addr=from_email, 
                                    to_addrs=to_email, 
                                    msg=message)
                print(f"Sending email to {to_email}..."
                    f" with message: {message}")
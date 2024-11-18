from bs4 import BeautifulSoup
import requests
from pprint import pprint
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Amazon
practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6",
            "Dnt": "1",
            "Priority": "u=1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

response = requests.get(url=live_url, headers=header)

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
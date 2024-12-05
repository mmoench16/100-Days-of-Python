from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, sys, requests

google_forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSfLD8uxTC45psIl0rIxQgMS_CnHwRsbGNrXtb2ZFPlFD9xw1A/viewform?usp=sf_link"
zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow_url)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")

listings = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

links = [listing.find("a").get("href") for listing in listings]
addresses = [listing.find("a").getText().strip() for listing in listings]
prices = [listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText() for listing in listings]

for idx, address in enumerate(addresses):
    addresses[idx] = address.replace(" | ", ", ").strip()

for idx, price in enumerate(prices):
    prices[idx] = price.replace("/mo", "").replace("+", "").replace("1 bd", "").replace("1bd", "").strip()

info = [links,addresses,prices]

# Keeps Chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(google_forms_url)

xpaths = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 
          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input']

for idx, link in enumerate(links):
    time.sleep(3)

    for i, xpath in enumerate(xpaths):
        input = driver.find_element(By.XPATH, value=xpath)
        input.click()
        input.send_keys(info[i][idx])

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(3)

    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
# driver.close() # closes the tab
driver.quit() # closes the browser
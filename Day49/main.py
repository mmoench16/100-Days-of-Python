from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Keeps Chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://www.linkedin.com/jobs/search/?currentJobId=4067575490&distance=25&f_AL=true&f_E=2&geoId=101596560&keywords=junior%20software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

driver = webdriver.Chrome(options=options)
driver.get(url)

# Click Reject Cookies Button
time.sleep(3)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Click Sign in Button
time.sleep(3)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='button[data-tracking-control-name="auth_wall_desktop_jserp-login-toggle"]')
sign_in_button.click()

# Fill in email and password
time.sleep(3)
email_field = driver.find_element(by=By.ID, value="username")
email_field = driver.find_element(by=By.CSS_SELECTOR, value='button[data-tracking-control-name="auth_wall_desktop_jserp-login-toggle"]')

email_field.send_keys(MY_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# driver.close() # closes the tab
# driver.quit() # closes the browser
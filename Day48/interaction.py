from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keeps Chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=options)
driver.get(url)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# Click on content portal
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" input by Name
# q_button = driver.find_element(By.CSS_SELECTOR, value="#p-search > a")
# q_button.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# Challenge
url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=options)
driver.get(url)

first_name_field = driver.find_element(By.NAME, value="fName")
first_name_field.send_keys("Martin")

last_name_field = driver.find_element(By.NAME, value="lName")
last_name_field.send_keys("Moench")

email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("martinm@example.com")

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()

# driver.quit() # closes the browser
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps Chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value = "a-price-fraction")

# price = float(price_dollar.text + "." + price_cents.text)
# print(f"The price is £{price}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_info = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li")
events = {i: {"date": event.find_element(By.TAG_NAME, value="time").get_attribute("datetime").split("T")[0], "name": event.find_element(By.TAG_NAME, value="a").text} for i, event in enumerate(event_info)}

print(events)

# for event in event_info:
#     print(event.find_element(By.TAG_NAME, value="a").text, event.find_element(By.TAG_NAME, value="time").get_attribute("datetime").split("T")[0])

# driver.close() # closes the current tab
driver.quit() # closes the browser
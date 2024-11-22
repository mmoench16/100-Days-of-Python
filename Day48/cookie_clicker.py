from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Keeps Chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=options)
driver.get(url)

def click_cookie():
    """
    Click the cookie to increase money.

    This function assumes that the cookie has been rendered
    and is clickable. No error checking is performed.

    Returns:
        None
    """
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

def get_money() -> int:
    """
    Get the current amount of money.

    This function assumes that the money field has been rendered
    and is visible. No error checking is performed.

    Returns:
        int: The current amount of money.
    """
    return int(driver.find_element(By.ID, value="money").text)

click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()
click_cookie()

time.sleep(1)

store = driver.find_element(By.ID, value="store")
items = store.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)
item_availability = ["grayed" not in item.get_attribute("class") for item in items]
print(item_availability)


# timeout = time.time() + 10 # 60*5+1
# time_interval = time.time() + 5

# while True:

#     click_cookie()
#     time.sleep(0.01)

#     if time.time() > time_interval:
#         money = get_money()
#         print(money)
#         time_interval = time.time() + 5
    
#     if time.time() > timeout:
#         break

# print(get_money())
# print("Done")
# driver.quit() # closes the browser

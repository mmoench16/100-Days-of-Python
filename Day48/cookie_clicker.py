from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
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


store = driver.find_element(By.ID, value="store")
items = store.find_elements(By.CSS_SELECTOR, value="#store div")
ITEM_IDS = [item.get_attribute("id") for item in items]

def get_store_items() -> pd.DataFrame:
    """
    Get the current store items.

    This function assumes that the store has been rendered and the
    items are visible. No error checking is performed.

    Returns:
        pd.DataFrame: A DataFrame containing the id, availability and
        price of each store item.
    """
    store = driver.find_element(By.ID, value="store")
    items = store.find_elements(By.CSS_SELECTOR, value="#store div")
    item_ids = [item.get_attribute("id") for item in items if item.get_attribute("id") in ITEM_IDS]
    print(item_ids)
    item_availability = ["grayed" not in item.get_attribute("class") for item in items if item.get_attribute("id") in ITEM_IDS]
    print(item_availability)
    item_prices = [item.find_element(By.CSS_SELECTOR, value="b").text for item in items if item.get_attribute("id") in ITEM_IDS]
    print(item_prices)

    for idx, item in enumerate(item_prices):
        if item == '':
            item_prices[idx] = 0
        else:
            item_prices[idx] = int(item.split("-")[1].strip().replace(",", ""))

    store_item_info = pd.DataFrame({
            'id': item_ids,
            'available': item_availability,
            'price': item_prices
    })

    return store_item_info

def best_available_upgrade(data: pd.DataFrame):
    best_upgrade = data[data['available'] == True].sort_values(by='price', ascending=False).iloc[0]

    return best_upgrade

timeout = time.time() + 60*1
time_interval = time.time() + 5

while True:

    click_cookie()

    if time.time() > time_interval:
        store_items = get_store_items()
        best_upgrade = best_available_upgrade(store_items)
        buy_item = driver.find_element(By.ID, value=best_upgrade.id)
        buy_item.click()
        print("Buying " + best_upgrade.id)
        time_interval = time.time() + 5
    
    if time.time() > timeout:
        break

cps = driver.find_element(By.ID, value="cps").text
print(cps)

# print(get_money())
# print("Done")
# driver.close() # closes the tab
# driver.quit() # closes the browser

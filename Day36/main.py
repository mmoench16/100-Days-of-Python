import os
import requests
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

text_belt_api_key = os.getenv("TEXTBELT_API_KEY")
recipient_number = os.getenv("RECIPIENT_NUMBER")

av_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": av_api_key
}

news_api_key = os.getenv("NEWS_API_KEY")
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "sortBy": "popularity",
    "pageSize": 3,
    "page": 1,
    "apiKey": news_api_key
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data_raw = response.json()
stock_data = list(stock_data_raw['Time Series (Daily)'].items())

y_closing_price = float(stock_data[0][1]['4. close'])

# Get the day before yesterday's closing stock price
dby_closing_price = float(stock_data[1][1]['4. close'])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(y_closing_price - dby_closing_price)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_perc = round(diff / dby_closing_price * 100, 2)

#If diff_perc percentage is greater than 5 then "Get News".
if diff_perc > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data_raw = response.json()
    news_data = news_data_raw['articles']

    print(news_data)

    # for article in news_data:
    #     resp = requests.post('https://textbelt.com/text', {
    #         'phone': recipient_number,
    #         'message': f"{STOCK_NAME}: {'⬆️' if diff > 0 else '⬇️'}{diff_perc}%\nHeadline: {article['title']}\nBrief: {article['description']}",
    #         'key': text_belt_api_key
    #         })
    #     resp.raise_for_status()
    #     print(resp.json())

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


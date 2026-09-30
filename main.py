STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from datetime import date, timedelta

def check_percentage(yest_price, before_price):
    perc_change = abs(yest_price - before_price)
    perc_change /= before_price
    perc_change *= 100
    print(perc_change)
    if perc_change >= 5:
        return True
    return False

yesterday_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_date = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d")
API_KEY = "GXC5CWBI99K7FQ97"
params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()
print(data)
close_price_one = float(data[yesterday_date]['4. close'])
close_price_two = float(data[day_before_date]['4. close'])
if check_percentage(close_price_one, close_price_two):
    print("Get news")




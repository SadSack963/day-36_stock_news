import requests
import os
import save_data
import json
import json

API_KEY = os.environ.get("APIKey-AlphaVantage")


def alpha_vantage_requests(stock):
    """
    Retrieve daily stock values.
    Return Last Refreshed Date, change in price, and change percentage.
    """
    base_url = "https://www.alphavantage.co/"
    endpoint = "query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": API_KEY,
    }

    url = base_url + endpoint

    response = requests.get(url=url, params=parameters, timeout=1)
    response.raise_for_status()

    daily = response.json()
    save_data.save_json(daily, "daily")

    # with open("./data/daily.json") as file:
    #     daily = json.load(fp=file)

    last_avail = daily["Meta Data"]["3. Last Refreshed"]

    list_daily = list(daily["Time Series (Daily)"].values())
    delta = float(list_daily[0]['4. close']) - float(list_daily[1]['4. close'])
    delta_percent = delta * 100 / float(list_daily[0]['4. close'])

    return last_avail, delta, delta_percent


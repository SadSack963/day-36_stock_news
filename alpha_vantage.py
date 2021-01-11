import requests
import os
import save_data


API_KEY = os.environ.get("APIKey-AlphaVantage")


def alpha_vantage_requests(stock):

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


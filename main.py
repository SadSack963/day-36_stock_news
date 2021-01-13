import os
import datetime
import alpha_vantage_get_prices
import newsapi_get_news
import dataframe
import send_email
import json
import time

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")


# TODO: STEP 1: Use Use https://www.alphavantage.co/documentation/#daily
#   When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#   HINT 1: Get the closing price for yesterday and the day before yesterday.
#     Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#   HINT 2: Work out the value of 5% of yesterday's closing stock price.

price_change = alpha_vantage_get_prices.alpha_vantage_requests(STOCK)
print(price_change)

# dataframe.plot_data(STOCK, COMPANY_NAME)


# TODO: STEP 2: Use https://newsapi.org/docs/endpoints/everything
#   Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#   HINT 1: Think about using the Python Slice Operator

if price_change[2] > 4.0:
    # newsapi_client.newsapi_client(STOCK, COMPANY_NAME)
    newsapi_get_news.newsapi_requests(STOCK, COMPANY_NAME)


# TODO: STEP 3: Use twilio.com/docs/sms/quickstart/python
#   Send a separate message with each article's title and description to your phone number.
#   HINT 1: Consider using a List Comprehension.

    with open("./data/everything.json") as file:
        everything = json.load(fp=file)

    for index in range(len(everything["articles"])):
        title = everything["articles"][index]["title"]
        description = everything["articles"][index]["description"]

        send_email.send_mail(
            STOCK,
            title,
            f"{price_change[0]}: {price_change[1]:.2f} points = {price_change[2]:.1f}%\n{description}"
        )
        time.sleep(5)

# TODO: Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors 
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions 
as of March 31st, near the height of the coronavirus market crash.

or

"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors 
are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions 
as of March 31st, near the height of the coronavirus market crash.
"""

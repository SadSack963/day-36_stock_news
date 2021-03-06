import alpha_vantage_get_prices
import newsapi_get_news
import graph
import send_email
import json
import os
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD = 4.0

load_dotenv("E:/Python/EnvironmentVariables/.env")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")


# API Document: https://www.alphavantage.co/documentation/#daily
# Retrieve daily stock prices
price_change = alpha_vantage_get_prices.alpha_vantage_requests(STOCK)
# print(price_change)

# Generate a boxplot of the stock prices (Open, High, Low, Close)
graph.plot_data(STOCK, COMPANY_NAME)
# print("boxplot done")

# API Document: https://newsapi.org/docs/endpoints/everything
# If the closing stock price increases or decreases by a given threshold
# between the last two days, then retrieve the top 3 news articles and send emails.
if abs(price_change[2]) >= THRESHOLD:
    # Get the top 3 news articles
    # newsapi_client.newsapi_client(STOCK, COMPANY_NAME)
    newsapi_get_news.newsapi_requests(STOCK, COMPANY_NAME)
    # print("news retrieved")

    # Send an email for each news article
    with open("./data/everything.json") as file:
        everything = json.load(fp=file)

    for index in range(len(everything["articles"])):
        title = everything["articles"][index]["title"]
        description = everything["articles"][index]["description"]
        url = everything["articles"][index]["url"]
        # urlToImage = everything["articles"][index]["urlToImage"]
        if price_change[1] > 0:
            indicator = "🔺"
        else:
            indicator = "🔻"
        subject = f"{STOCK}:{indicator} {price_change[2]:.1f}% {title}"
        message = f"{price_change[0]}: " \
                  f"{STOCK} - " \
                  f"{COMPANY_NAME}. " \
                  f"{indicator} " \
                  f"{price_change[1]:.2f} points = " \
                  f"{price_change[2]:.1f}%\n" \
                  f"{description}\n\n" \
                  f"{url}\n"
        # print(message)

        send_email.send_mail(
            subject,
            message
        )
        # print("email sent")

# TODO: Optional: Use twilio.com/docs/sms/quickstart/python
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

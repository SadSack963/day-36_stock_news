import smtplib
import datetime as dt
import random
import os

# Encoding email headers
# https://docs.python.org/3/library/email.header.html
from email.message import Message
from email.header import Header


# # https://nerderati.com/2017/06/09/mime-encoded-words-in-email-headers/
# import email
# from email.header import decode_header
#
# result = decode_header(
#     u'=?UTF-8?Q?TSLA=3a=e2=ac=86-8=25_=2cTesla_Inc=2e_stock_rises_Thursda?= \
#     =?UTF-8?Q?y=2c_outperforms_market?='
# )
# print(result)
# """
# Output: [(b'TSLA:\xe2\xac\x86-8% ,Tesla Inc. stock rises Thursday, outperforms market', 'utf-8')]
# """
#
# print(result[0][0].decode(result[0][1]))
# """
# Output: TSLA:⬆-8% ,Tesla Inc. stock rises Thursday, outperforms market
# """


YAHOO_SENDER = os.environ.get("SMTP_YAHOO_SENDER")
YAHOO_USERNAME = os.environ.get("SMTP_YAHOO_USERNAME")
YAHOO_EMAIL = os.environ.get("SMTP_YAHOO_EMAIL")
YAHOO_PASSWORD = os.environ.get("SMTP_YAHOO_PASSWORD")
YAHOO_RECIPIENT = os.environ.get("SMTP_YAHOO_RECIPIENT")


def send_mail(stock, headline, description):
    # SEND FROM YAHOO ACCOUNT

    # Encode email Subject header
    msg = Message()
    h = Header(f"{stock}: {headline}", "utf-8")
    msg['Subject'] = h
    # print(msg.as_string())
    """
    Subject: =?utf-8?q?TSLA=3A=E2=AC=86-8=25_=2CTesla_Inc=2E_stock_rises_Thursday=2C_outperforms_market?=
    """

    # Compile the message
    message = f"From: \"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>\n" \
              f"To: {YAHOO_RECIPIENT}\n" \
              f"{msg.as_string()}\n\n" \
              f"{description}".encode("utf-8")
    print(message)

    # Send the email
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message)





import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os
from dotenv import load_dotenv

# Encoding email headers
# https://docs.python.org/3/library/email.header.html

load_dotenv("E:/Python/EnvironmentVariables/.env")
YAHOO_SENDER = os.getenv("SMTP_YAHOO_SENDER")
YAHOO_USERNAME = os.getenv("SMTP_YAHOO_USERNAME")
YAHOO_EMAIL = os.getenv("SMTP_YAHOO_EMAIL")
YAHOO_PASSWORD = os.getenv("SMTP_YAHOO_PASSWORD")
YAHOO_RECIPIENT = os.getenv("SMTP_YAHOO_RECIPIENT")


def send_mail(header, description):
    # SEND FROM YAHOO ACCOUNT

    # Compile email headers
    # Subject is encoded to allow non-ASCII characters (RFC2047)
    message = MIMEMultipart()
    message["From"] = f"\"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>"
    message["To"] = f"{YAHOO_RECIPIENT}"
    message["Subject"] = Header(s=header, charset="utf-8")
    # message["Bcc"] = f"{YAHOO_RECIPIENT}"

    # Add the text message
    msg_text = MIMEText(_text=f"{description}", _subtype="plain", _charset="utf-8")
    message.attach(msg_text)

    # Add an image as attachment
    with open('./images/boxplot.png', 'rb') as file:
        img = MIMEImage(file.read())
        img.add_header('Content-Disposition', 'attachment', filename="boxplot.png")
        message.attach(img)

    # print(message)

    # Send the email
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message.as_string())





import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_USER = os.getenv('SERVICE_USER')
SERVICE_PASSWORD = os.getenv('SERVICE_PASSWORD')
TARGET_EMAIL_ADDRESS = os.getenv('TARGET_EMAIL_ADDRESS')

port = 465 # for ssl

message = """
Subject: Test Message

This message was sent programmatically!
"""

# create secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(SERVICE_USER, SERVICE_PASSWORD)
    server.sendmail(SERVICE_USER, TARGET_EMAIL_ADDRESS, message)
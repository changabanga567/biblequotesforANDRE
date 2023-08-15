# src/sms_sender.py

from twilio.rest import Client
from config import settings

def send_sms(message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    response = client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=settings.DESTINATION_PHONE_NUMBER
    )

    return response.sid

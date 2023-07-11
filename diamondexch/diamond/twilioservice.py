from django.conf import settings
from twilio.rest import Client
# from twilio.http import j


class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_via_message(self):

        client = Client(settings.API_KEY_SID,
                        settings.API_SECRET, settings.ACCOUNT_SID)
        message = client.messages.create(
            body=f"Your otp is:{self.otp}", from_=f"{settings.TWILIO_PHONE_NUMBER}", to=f"{settings.COUNTRY_CODE}{self.phone_number}")

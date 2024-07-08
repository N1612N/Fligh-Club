import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    """This class is responsible for sending notifications with the offer flight ticket details to the user."""
    def __init__(self):
        self.twilio_account_sid = os.getenv("twilio_account_sid")
        self.twilio_auth_token = os.getenv("twilio_auth_token")
        self.twilio_from_number = os.getenv("twilio_from_number")
        self.twilio_to_number = os.getenv("twilio_to_number")
        self.from_addr = os.getenv("from_addr")
        self.app_password = os.getenv("app_password")

    def send_mesg(self, data):
        """Sends an SMS to the user with fight ticket offer details"""
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        twilio_message = client.messages.create(
            from_=self.twilio_from_number,
            body=data,
            to=self.twilio_to_number
        )
        print(f"[+] SMS has been {twilio_message.status} to {self.twilio_to_number}")

    def send_mail(self, cust_email_addr, message_body):
        """Send emails to all the user in spreadsheet with fight ticket offer details"""
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.from_addr, password=self.app_password)
            connection.sendmail(
                from_addr=self.from_addr,
                to_addrs=cust_email_addr,
                msg=f"Subject: Fly with Coconut Holidays! \n\n {message_body}"
            )
            print(f"[+] Sending Email to {cust_email_addr} !")

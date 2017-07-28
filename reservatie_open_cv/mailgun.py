from requests import post
from lab9k.settings import MAILGUN_API_KEY


def send_async_message(from_email, to_email, subject, text):
    return post(
        "https://api.mailgun.net/v3/mail.lab9k.gent/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": from_email,
              "to": [to_email],
              "subject": subject,
              "text": text})

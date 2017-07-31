from requests import post
from lab9k.settings import MAILGUN_API_KEY


def send_async_message(from_email, to_email, subject, text):
    """
    Sends an email with the mailgun api (<a href="https://www.mailgun.com/">mailgun</a> )
    :param from_email: mailgun email address the mail will be sent from
    :param to_email: email address the email will be sent to
    :param subject: subject of the email
    :param text: text of the email
    :return: requests.Reponse
    """
    return post(
        "https://api.mailgun.net/v3/mail.lab9k.gent/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": from_email,
              "to": [to_email],
              "subject": subject,
              "text": text})

from django.core.mail import EmailMessage
from logging import info, error
from random import randint

from .models import OTP_RANGE


def send_confirmation_code(email, code):
    subject = "Email Verification"
    message = f"Your confirmation code is: {code}"

    try:
        email_message = EmailMessage(subject=subject, body=message, to=[email])
        response = email_message.send(fail_silently=False)
        info(f"response is {response}")
    except Exception as error:
        error(f"{error} when sending email to {email}")


def generate_confirmation_code():
    start, end = OTP_RANGE
    random_otp = randint(start, end)
    return random_otp

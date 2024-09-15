from django.forms import EmailField
from django.core.exceptions import ValidationError
from .models import (
    MAX_EMAIL_CHAR,
    MAX_USERNAME_CHAR,
    MIN_USERNAME_CHAR,
    MIN_PASSWORD_CHAR,
)


def is_email_valid(email):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False


def is_username_valid(username):
    if MIN_USERNAME_CHAR <= len(username) <= MAX_USERNAME_CHAR:
        return True
    else:
        return False


def is_password_valid(password1, password2):
    return len(password1) >= MIN_PASSWORD_CHAR and (password1 == password2)

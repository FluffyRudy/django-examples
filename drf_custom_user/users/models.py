from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .managers import UserManager

MAX_USERNAME_CHAR = 25
MIN_USERNAME_CHAR = 4
MIN_PASSWORD_CHAR = 8
MAX_EMAIL_CHAR = 50
CONFIRMTION_CODE_RANGE = 8
OTP_RANGE = (10_000_000, 99_999_999)


def confirmation_code_validator(code):
    if code is not None and (OTP_RANGE[0] <= code < OTP_RANGE[1]):
        raise ValidationError("Invalid confirmation code, must be exactly length of 8")


class CustomUser(AbstractUser):
    username = models.CharField(max_length=MAX_USERNAME_CHAR, unique=True)
    email = models.EmailField(unique=True, max_length=MAX_EMAIL_CHAR)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.IntegerField(
        null=True, blank=True, validators=[confirmation_code_validator]
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

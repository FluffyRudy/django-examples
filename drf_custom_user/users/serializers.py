from django.core.validators import EmailValidator
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomUser
from . import validators


class UserRegistrationSerializer(ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def create(self, validated_data):
        email = validated_data.pop("email")
        username = validated_data.get("username")
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")

        return CustomUser.objects.create_user(
            email=email, password=password1, **validated_data
        )

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if not validators.is_username_valid(username):
            message = "Username must be at least 4 character long"
            raise ValidationError(message)
        if not validators.is_password_valid(password1, password2):
            message = (
                "Length of password must be at least 8 character long and should match"
            )
            raise ValidationError(message)
        elif not validators.is_email_valid(email):
            message = f"Invalid email: {email}, please enter valid email"
            raise ValidationError(message)

        return attrs

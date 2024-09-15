import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

from .models import CustomUser
from . import serializers
from . import utils


class HomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({"message": f"welcome {request.user.username}"})


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserRegistrationSerializer


class ConfirmationCodeRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user: CustomUser = request.user
        if user.email is None:
            return Response(
                {"message": "User not found error"}, status=status.HTTP_404_NOT_FOUND
            )
        if user.is_confirmed:
            return Response({"message": "You are already verified"})
        confirmation_code = utils.generate_confirmation_code()
        user.confirmation_code = confirmation_code
        user.save()
        utils.send_confirmation_code(user.email, confirmation_code)

        return Response({"message": f"confirmation code sent at {user}"})


class VerifyConfirmationCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print("er")
        email = request.user.email

        if not email:
            return Response({"message": "Email not found"})

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        confirmation_code = user.confirmation_code

        if confirmation_code is None:
            return Response({"message": "request for code berfore verifying "})

        if user.confirmation_code == confirmation_code:
            user.is_confirmed = True
            user.confirmation_code = None
            user.save()
            return Response({"message": "Your email has been verified successfully."})
        else:
            return Response(
                {"message": "Invalid confirmation code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

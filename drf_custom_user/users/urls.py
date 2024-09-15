from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.HomeView.as_view(), name="home"),
    path("api/users/create/", views.UserRegistrationView.as_view(), name="register"),
    path(
        "api/users/verify/request/",
        views.ConfirmationCodeRequestView.as_view(),
        name="request-verification",
    ),
    path(
        "api/users/verify/",
        views.VerifyConfirmationCodeView.as_view(),
        name="verify-user",
    ),
]

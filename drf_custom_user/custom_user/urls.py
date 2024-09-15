from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tokens/", view=TokenObtainPairView.as_view(), name="tokens"),
    path("tokens/refresh/", view=TokenRefreshView.as_view(), name="refresh"),
    path("", include("users.urls")),
]

from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    UserChangePasswordView,
    UserProfileRegistrationView,
    UserProfileRetrieveUpdateView,
)

urlpatterns = [
    path("user", UserProfileRetrieveUpdateView.as_view(), name="user"),
    path("user/register", UserProfileRegistrationView.as_view(), name="register"),
    path("user/login", TokenObtainPairView.as_view(), name="login"),
    path("user/token/refresh", TokenRefreshView.as_view()),
    path(
        "user/change-password", UserChangePasswordView.as_view(), name="change_password"
    ),
]

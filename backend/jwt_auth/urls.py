from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    UserChangePasswordView,
    UserProfileRegistrationView,
    UserProfileRetrieveUpdateView,
)

urlpatterns = [
    path("", UserProfileRetrieveUpdateView.as_view(), name="user"),
    path("register", UserProfileRegistrationView.as_view(), name="register"),
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh", TokenRefreshView.as_view()),
    path("change-password", UserChangePasswordView.as_view(), name="change_password"),
]

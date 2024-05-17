from django.urls import path
from rest_framework.routers import DefaultRouter
from fj_finance_tracker.users.api.views import (
    RegistrationView,
    LoginView,
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
]
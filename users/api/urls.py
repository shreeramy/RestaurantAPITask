from django.urls import path
from .api_views import UserCreateView, UserOTPView, EmployeeCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("account_register/", UserCreateView.as_view()),
    path('otp_verification/',UserOTPView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path("employee_create/", EmployeeCreateView.as_view()),
]

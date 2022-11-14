from django.urls import path
from .api_views import UserCreateView, UserOTPView, EmployeeCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("account_register/", UserCreateView.as_view(), name='account_register'),
    path('otp_verification/',UserOTPView.as_view(), name='otp_verification'),
    path('api/token/', TokenObtainPairView.as_view(), name='access_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token' ),
    path("employee_create/", EmployeeCreateView.as_view(), name='employee_create'),
]

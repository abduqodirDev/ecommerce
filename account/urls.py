from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import UserCreateView, VerificationOtpView, LoginView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('verify/', VerificationOtpView.as_view(), name='verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import UserCreateView, VerificationOtpView, LoginView, PasswordResetView,\
PasswordResetVerifyView, PasswordResetFinishView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('verify/', VerificationOtpView.as_view(), name='verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('password-reset/start/', PasswordResetView.as_view(), name='password-reset-start'),
    path('password-reset/verify/', PasswordResetVerifyView.as_view(), name='password-reset-verify'),
    path('password-reset/finish/', PasswordResetFinishView.as_view(), name='password-reset-finish'),
]

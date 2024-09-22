from django.urls import path

from account.views import UserCreateView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register')
]

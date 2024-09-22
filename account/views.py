from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from account.models import User
from account.serializers import UserCreateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        password = serializer.data['password']
        user.set_password(password)
        user.save()


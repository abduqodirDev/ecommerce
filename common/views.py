from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Media
from .serializers import MediaSerializer


class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

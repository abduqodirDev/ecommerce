from django.urls import path

from .views import MediaListAPIView


urlpatterns = [
    path('media/', MediaListAPIView.as_view(), name='media')
]



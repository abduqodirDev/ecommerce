from django.urls import path

from .views import CategoryListAPIView, ProductListAPIView, ProductColorListView, ProductSizeListView


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('colors/', ProductColorListView.as_view(), name='colors'),
    path('sizes/', ProductSizeListView.as_view(), name='sizes'),
]

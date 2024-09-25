from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import CategoryListSerializer, ProductListSerializer
from .models import Category, Product


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

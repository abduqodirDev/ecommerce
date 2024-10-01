from django.urls import path

from order.views import AddToCartView, UpdateCartItemView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('update-to-cart/<int:pk>/', UpdateCartItemView.as_view(), name='update-to-cart'),
]
